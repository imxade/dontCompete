#!/usr/bin/env python3
"""
Compare classification results from multiple Ollama models.
Analyzes response quality and recommends the best model.
"""
import os
import json
import glob
from collections import defaultdict

# Get the absolute path to the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def analyze_model_responses(model_name):
    """Analyze responses from a specific model."""
    model_safe = model_name.replace(':', '_').replace('/', '_')
    response_dir = os.path.join(BASE_DIR, "data", "responses", model_safe)
    
    if not os.path.exists(response_dir):
        return None
    
    stats = {
        "model": model_name,
        "total_responses": 0,
        "valid_json": 0,
        "total_questions_classified": 0,
        "total_subtopics": 0,
        "avg_questions_per_response": 0,
        "errors": []
    }
    
    response_files = glob.glob(f"{response_dir}/*.json")
    stats["total_responses"] = len(response_files)
    
    all_questions = set()
    all_subtopics = set()
    
    for filepath in response_files:
        try:
            with open(filepath, 'r') as f:
                content = f.read().strip()
                
            # Remove markdown code blocks if present
            if content.startswith('```'):
                content = content.split('```')[1]
                if content.startswith('json'):
                    content = content[4:]
                content = content.strip()
            
            data = json.loads(content)
            stats["valid_json"] += 1
            
            # Count questions and subtopics
            for subject, subtopics in data.items():
                if isinstance(subtopics, dict):
                    for subtopic, questions in subtopics.items():
                        all_subtopics.add(f"{subject}/{subtopic}")
                        if isinstance(questions, list):
                            all_questions.update(questions)
                        
        except json.JSONDecodeError as e:
            stats["errors"].append(f"{os.path.basename(filepath)}: JSON error")
        except Exception as e:
            stats["errors"].append(f"{os.path.basename(filepath)}: {str(e)}")
    
    stats["total_questions_classified"] = len(all_questions)
    stats["total_subtopics"] = len(all_subtopics)
    
    if stats["valid_json"] > 0:
        stats["avg_questions_per_response"] = stats["total_questions_classified"] / stats["valid_json"]
    
    return stats

def compare_models():
    """Compare all available model results."""
    response_base = os.path.join(BASE_DIR, "data", "responses")
    
    if not os.path.exists(response_base):
        print("No response directory found!")
        return
    
    # Find all model directories
    model_dirs = [d for d in os.listdir(response_base) if os.path.isdir(os.path.join(response_base, d))]
    
    if not model_dirs:
        print("No model results found!")
        return
    
    print("=" * 60)
    print("MULTI-MODEL COMPARISON")
    print("=" * 60)
    print()
    
    results = []
    for model_dir in model_dirs:
        # Convert directory name back to model name
        model_name = model_dir.replace('_', ':', 1).replace('_', '/')
        stats = analyze_model_responses(model_name)
        
        if stats:
            results.append(stats)
            
            print(f"Model: {stats['model']}")
            print(f"  Total Responses: {stats['total_responses']}")
            print(f"  Valid JSON: {stats['valid_json']}")
            print(f"  Questions Classified: {stats['total_questions_classified']}")
            print(f"  Subtopics Extracted: {stats['total_subtopics']}")
            print(f"  Avg Questions/Response: {stats['avg_questions_per_response']:.1f}")
            if stats['errors']:
                print(f"  Errors: {len(stats['errors'])}")
                for err in stats['errors'][:3]:
                    print(f"    - {err}")
            print()
    
    if not results:
        print("No valid results to compare!")
        return
    
    # Rank models
    print("=" * 60)
    print("RANKING")
    print("=" * 60)
    print()
    
    # Sort by total questions classified (primary) and subtopics (secondary)
    ranked = sorted(results, key=lambda x: (x['total_questions_classified'], x['total_subtopics']), reverse=True)
    
    for i, stats in enumerate(ranked, 1):
        print(f"{i}. {stats['model']}")
        print(f"   Score: {stats['total_questions_classified']} questions, {stats['total_subtopics']} subtopics")
        print()
    
    # Recommend best
    best = ranked[0]
    print("=" * 60)
    print(f"RECOMMENDED MODEL: {best['model']}")
    print("=" * 60)
    print(f"Classified {best['total_questions_classified']} questions into {best['total_subtopics']} subtopics")
    print(f"Success rate: {best['valid_json']}/{best['total_responses']} responses")
    print()
    
    # Update config recommendation
    print("To use this model, set in your environment:")
    print(f"  export OLLAMA_MODEL='{best['model']}'")
    print()

if __name__ == "__main__":
    compare_models()
