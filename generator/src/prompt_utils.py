import os
import logging
import fitz
from generator.src.config import CLASSIFICATION_BATCH_SIZE
from generator.src.text_utils import slugify

logger = logging.getLogger(__name__)

PROMPT_DIR = os.path.join('data', 'prompts')
os.makedirs(PROMPT_DIR, exist_ok=True)

def _read_syllabus(stream_code):
    """Read and return syllabus text for a stream."""
    from generator.src.config import STREAM_ALIASES, RAW_DATA_DIR
    stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
    syllabus_path = os.path.join(RAW_DATA_DIR, stream_alias, 'syllabus.pdf')
    
    if not os.path.exists(syllabus_path):
        logger.error(f"Syllabus not found: {syllabus_path}")
        return None
        
    try:
        doc = fitz.open(syllabus_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        logger.error(f"Failed to read syllabus: {e}")
        return None
    
def generate_classification_prompts(con, stream_code, batch_size=None, max_batches=None):
    """
    Generates classification prompts with syllabus + questions per batch.
    Each prompt is self-contained with full context.
    """
    from generator.src.config import STREAM_ALIASES
    stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
    
    if batch_size is None:
        batch_size = CLASSIFICATION_BATCH_SIZE
    
    # 1. Read Syllabus
    syllabus_text = _read_syllabus(stream_code)
    if not syllabus_text:
        logger.warning(f"Cannot generate classification prompts without syllabus for {stream_code}")
        return []
    
    # 2. Fetch All Questions for this stream
    questions = con.execute("""
        SELECT id, q_text 
        FROM questions 
        WHERE stream_code = ?
    """, (stream_code,)).fetchall()
    
    if not questions:
        logger.info(f"No questions found for {stream_code}")
        return []
    
    logger.info(f"Found {len(questions)} questions for {stream_code}")
        
    # 3. Generate Batched Prompts
    generated_files = []
    batch_num = 0
    
    for i in range(0, len(questions), batch_size):
        if max_batches and batch_num >= max_batches:
            logger.info(f"Reached max_batches limit of {max_batches}")
            break
            
        batch = questions[i:i+batch_size]
        
        # Create question list with clean IDs and numbers
        q_list = []
        for idx, q in enumerate(batch, 1):
            # Clean the question ID (remove trailing periods)
            clean_id = q[0].rstrip('.')
            q_list.append(f"{idx}. ID={clean_id}\n   {q[1][:400]}")
        
        q_context = "\n\n".join(q_list)
        all_question_ids = [q[0].rstrip('.') for q in batch]
        
        prompt = f"""You are a highly meticulous GATE exam classifier. Your task is to accurately categorize questions into the provided syllabus structure.

SYLLABUS:
{syllabus_text}

ADDITIONAL VALID CATEGORIES:
Section GA: General Aptitude
- Verbal Ability: English grammar, sentence completion, verbal analogies, word groups, instructions, critical reasoning and verbal deduction.
- Numerical Ability: Numerical computation, numerical estimation, numerical reasoning and data interpretation.
- Spatial Aptitude: Transformation of shapes (translation, rotation, scaling, mirroring, assembling, grouping), paper folding, cutting, and patterns in 2D and 3D.

Section Other: Unclassifiable
- STRICT WARNING: Use this category ONLY if the question is completely irrelevant to the syllabus (e.g., a question about cooking in a CS exam). 
- If a question has ANY technical keywords that appear in the syllabus, you MUST find a match. 
- Misclassifying a valid syllabus question as "Other" is a failure.

QUESTIONS TO CLASSIFY:
{q_context}

YOUR TASK:
For each question:
1. **Analyze (Thinking)**: Break down the question, identify core concepts, and match them against the syllabus keywords.
2. **Classify**: Map it to a Subject and a specific Subtopic.
3. **Format**: Use the exact question ID (the ID= value shown above).

PROCESS:
1. First, provide a `<thinking>` section where you briefly analyze each question (max 2 sentences per question).
2. Then, provide the final result in a single JSON block.

CRITICAL RULES:
1. **Think First**: Use the `<thinking>` tag before the JSON.
2. **No Lazy Mapping**: Do not use "Other" unless you have tried matching against every single syllabus item.
3. **Exact Names**: Use subtopic names EXACTLY as they appear in the syllabus.
4. **All Questions**: Include ALL {len(batch)} question IDs exactly as shown.
5. **JSON Only**: After the thinking section, output ONLY the JSON object. No explanations.

Example Output:
<thinking>
1. ID={all_question_ids[0]}: Analyzed concepts X and Y. These are fundamental to Boolean Algebra in Digital Logic.
2. ID={all_question_ids[1]}: Topic involves English grammar, which fits under General Aptitude -> Verbal Ability.
</thinking>

{{
  "Digital Logic": {{
    "Boolean Algebra": ["{all_question_ids[0]}"]
  }},
  "General Aptitude": {{
    "Verbal Ability": ["{all_question_ids[1]}"]
  }}
}}

JSON OUTPUT:
"""
        filename = f"classify_{stream_alias}_batch_{batch_num}.txt"
        filepath = os.path.join(PROMPT_DIR, filename)
        
        with open(filepath, 'w') as f:
            f.write(prompt)
        generated_files.append(filepath)
        batch_num += 1
        
    logger.info(f"Generated {len(generated_files)} classification prompts for {stream_code}")
    return generated_files

def generate_theory_prompts(con, stream_code):
    """Generate theory prompts for each subtopic with all its questions."""
    from generator.src.config import STREAM_ALIASES
    stream_alias = STREAM_ALIASES.get(stream_code, stream_code)
    
    # Fetch subtopics with their questions
    subtopics = con.execute("""
        SELECT 
            st.id,
            st.name,
            s.name as subject_name,
            s.stream_code,
            COUNT(q.id) as question_count
        FROM subtopics st
        JOIN subjects s ON st.subject_id = s.id
        LEFT JOIN questions q ON q.subtopic_id = st.id
        WHERE s.stream_code = ?
        GROUP BY st.id, st.name, s.name, s.stream_code
        HAVING question_count > 0
    """, (stream_code,)).fetchall()
    
    generated_files = []
    
    for subtopic_id, subtopic_name, subject_name, st_code, q_count in subtopics:
        # Get all questions for this subtopic
        questions = con.execute("""
            SELECT id, q_text, a_text
            FROM questions
            WHERE subtopic_id = ?
        """, (subtopic_id,)).fetchall()
        
        if not questions:
            logger.info(f"No questions for subtopic {subtopic_name}, skipping theory generation")
            continue
        
        # Format questions
        q_context = "\n\n".join([f"Q{i+1} (ID: {q[0]}):\nQ: {q[1][:800]}\nA: {q[2][:300]}" for i, q in enumerate(questions)])
        
        # Check for existing theory file
        from generator.src.config import GATE_ASSETS_DIR
        import re
        
        subj_slug = slugify(subject_name, normalize=True)
        topic_slug = slugify(subtopic_name, normalize=True)
        existing_md_path = os.path.join(GATE_ASSETS_DIR, stream_alias, subj_slug, f"{topic_slug}.md")
        
        existing_content = ""
        existing_instruction = ""
        
        if os.path.exists(existing_md_path):
            with open(existing_md_path, 'r') as f:
                existing_content = f.read()
            
            existing_instruction = f"""
EXISTING THEORY CONTENT:
Below is the previously generated theory for this topic.
--------------------------------------------------
{existing_content}
--------------------------------------------------

TASK: IMPROVE and EXPAND the existing content above.
1. **Preserve**: Keep all correct and relevant information.
2. **Expand**: Add missing details, more depth on complex topics, and better explanations.
3. **Refine**: Fix any inaccuracies or unclear sections.
4. **Augment**: Add more examples and diagrams if they are missing.
"""
        else:
            existing_instruction = "TASK: Create a comprehensive Theory Note from scratch."

        prompt = f"""You are an expert GATE CS exam tutor. {existing_instruction}

TOPIC: {subtopic_name}
SUBJECT: {subject_name}
CONTEXT: This topic has {len(questions)} previous year questions.

GOAL: Create/Update a high-quality, exam-focused study note that covers all theoretical concepts, formulas, and insights required to solve the questions below and similar future questions.

SOURCE QUESTIONS (Analyze these to determine depth and scope):
{q_context}

INSTRUCTIONS:
1. **Format**: Use strict Markdown.
2. **Structure**:
   - **Introduction**: Brief overview of the concept.
   - **Core Concepts**: Detailed explanation of principles, laws, or algorithms.
   - **Key Formulas/Theorems**: Use LaTeX for math (e.g., $E=mc^2$).
   - **Problem Solving Patterns**: specific techniques derived from the source questions.
   - **Examples with Solutions**: Provide clear, step-by-step examples.
   - **Common Pitfalls**: What do students often miss?
   - **Quick Summary**: Bullet points for revision.
3. **Visuals**:
   - Use **Mermaid diagrams** for logic, flows, or structures where applicable.
     ```mermaid
     graph LR
     A[Start] --> B[Process]
     ```
   - **Online Images**: You MAY include external image URLs (e.g., Wikimedia Commons, reliable educational sites) if and ONLY IF you are confident they are stable and accurate.
     Format: `![Description](https://example.com/image.png)`
4. **Style**: Concise, high-yield, technical but accessible. Avoid fluff.
5. **Coverage**: Ensure EVERY concept tested in the source questions is explained in the theory.

OUTPUT:
Return the Markdown content ONLY.
"""
        
        # Filename: theory_{subtopic_id}.txt
        # subtopic_id is unique (e.g., cs_subj_1_topic_1)
        filename = f"theory_{subtopic_id}.txt"
        filepath = os.path.join(PROMPT_DIR, filename)
        
        with open(filepath, 'w') as f:
            f.write(prompt)
        generated_files.append(filepath)
    
    logger.info(f"Generated {len(generated_files)} theory prompts for {stream_code}")
    return generated_files
