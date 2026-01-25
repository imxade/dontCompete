
import re

def normalize_subtopic(name):
    """Normalizes subtopic name to reduce duplicates."""
    if not name: return ""
    
    # 1. Lowercase
    name = name.lower()
    
    # 2. Replace symbols and separators with spaces
    name = name.replace('&', ' and ').replace('+', ' plus ')
    name = re.sub(r'[/\-_]', ' ', name)
    
    # 3. Remove punctuation (keep alphanumeric and spaces)
    name = re.sub(r'[^\w\s]', '', name)
    
    # 4. Collapse multiple spaces and strip
    name = ' '.join(name.split())
    
    # 5. Remove generic words
    stop_words = {'system', 'systems'}
    words = name.split()
    words = [w for w in words if w not in stop_words]
    name = ' '.join(words)
    
    # 6. Remove trailing 's'
    # Exclude common endings that are NOT plural markers (ss, is, us, as)
    if name.endswith('s') and not any(name.endswith(x) for x in ['ss', 'is', 'us', 'as']):
        if len(name) > 3: # Avoid mangling short words like 'bus' or 'dns' (though bus ends in us)
            name = name[:-1]
        
    return name.strip()

def slugify(text):
    """Converts text to a slug."""
    res = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower()).strip('-')
    if len(res) > 80:
        res = res[:80].strip('-')
    return res
