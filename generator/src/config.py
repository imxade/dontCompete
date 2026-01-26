import os

# Environment Configuration
# Local LLM Only

# Ollama Configuration
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3.1')  # Model to use for local LLM

# Ollama Host
_OLLAMA_HOST_ENV = os.getenv('OLLAMA_HOST')
if _OLLAMA_HOST_ENV:
    if _OLLAMA_HOST_ENV.startswith('http'):
        OLLAMA_BASE_URL = _OLLAMA_HOST_ENV
    else:
        OLLAMA_BASE_URL = f"http://{_OLLAMA_HOST_ENV}"
else:
    OLLAMA_BASE_URL = "http://localhost:11434"


# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(BASE_DIR)

# Data Directories
DATA_DIR = os.path.join(REPO_ROOT, 'data')
GATE_ASSETS_DIR = os.path.join(REPO_ROOT, 'frontend', 'public', 'assets', 'gate')

RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
DB_PATH = os.path.join(DATA_DIR, 'app.duckdb')


STREAM_ALIASES = {
    'computer-science-information-technology': 'cs',
    'data-science-artificial-intelligence': 'da',
    'electrical-engineering': 'ee',
    'mechanical-engineering': 'me',
    'electronics-and-communication-engineering': 'ec',
    'instrumentation-engineering': 'in',
    'civil-engineering': 'ce',
    'chemical-engineering': 'ch'
}

# Set Limitations

# Limit number of prompts for testing. Comment out for full run.
TEST_PROMPT_LIMIT = None  
# TEST_PROMPT_LIMIT = 1  

# Questions per classification prompt
CLASSIFICATION_BATCH_SIZE = int(os.getenv('CLASSIFICATION_BATCH_SIZE', '10'))  
assert CLASSIFICATION_BATCH_SIZE > 0, "CLASSIFICATION_BATCH_SIZE must be positive"

# Scraping Configuration
TARGET_STREAMS = [
    # 'data-science-artificial-intelligence',
    # 'electrical-engineering',
    # 'mechanical-engineering',
    # 'electronics-and-communication-engineering',
    # 'instrumentation-engineering',
    # 'civil-engineering',
    # 'chemical-engineering',
    'computer-science-information-technology',
]

GATE_ACADEMY_URL = "https://www.gateacademy.co.in"
