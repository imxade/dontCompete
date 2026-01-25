#!/usr/bin/env python3
"""
Test multiple Ollama models and select the best one.
Runs classification with different models and compares results.
"""
import subprocess
import os
import sys
import time

# Models to test (4-5GB range, good for classification)
MODELS_TO_TEST = [
    "qwen", 
    "llama3.1",
    "mistral"
]

# Get the absolute path to the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_model_test(model_name):
    """Run classification test with a specific model."""
    print(f"\n{'='*60}")
    print(f"Testing model: {model_name}")
    print(f"{'='*60}\n")
    
    # Set environment variable for this model
    env = os.environ.copy()
    env['OLLAMA_MODEL'] = model_name
    
    try:
        # Run docker compose with the model
        result = subprocess.run(
            ['docker', 'compose', 'up', 'asset-generator'],
            env=env,
            cwd=BASE_DIR,
            capture_output=False,
            text=True
        )
        
        print(f"\nCompleted test for {model_name}")
        print(f"Exit code: {result.returncode}\n")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"Error testing {model_name}: {e}")
        return False

def compare_results():
    """Compare results from all models and recommend the best."""
    print(f"\n{'='*60}")
    print("ANALYZING RESULTS")
    print(f"{'='*60}\n")
    
    # Run the comparison script
    try:
        subprocess.run(
            ['python3', 'compare_models.py'],
            cwd=BASE_DIR,
            check=True
        )
    except Exception as e:
        print(f"Error comparing results: {e}")

def main():
    """Main test orchestration."""
    print("Starting Multi-Model Classification Test")
    print(f"Testing {len(MODELS_TO_TEST)} models: {', '.join(MODELS_TO_TEST)}\n")
    
    results = {}
    
    for model in MODELS_TO_TEST:
        success = run_model_test(model)
        results[model] = success
        
        if not success:
            print(f"WARNING: Test failed for {model}")
        
        # Small delay between tests
        time.sleep(2)
    
    # Show summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}\n")
    
    for model, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{model}: {status}")
    
    # Compare results
    compare_results()

if __name__ == "__main__":
    main()
