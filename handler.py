import runpod
import os
import time

# --- Configuration ---
# You can use environment variables to control model paths or settings
MODEL_NAME = os.environ.get("MODEL_NAME", "example-model")

# --- Global Model Variable ---
# We define the model variable in the global scope.
# This ensures it persists across multiple calls to the handler (Warm Start).
MODEL = None

def load_model():
    """
    Load your model here.
    This function runs once when the container starts or when the first job is received.
    """
    print(f"Loading model: {MODEL_NAME}...")
    
    # ------------------------------------------------------------------
    # REPLACE THIS BLOCK WITH YOUR ACTUAL MODEL LOADING LOGIC
    # Example:
    # import torch
    # from transformers import pipeline
    # return pipeline("text-generation", model=MODEL_NAME, device=0)
    # ------------------------------------------------------------------
    
    # Simulating a model load time
    time.sleep(2) 
    print("Model loaded successfully.")
    
    # Return your loaded model object
    return "DUMMY_MODEL_OBJECT"

def handler(job):
    """
    The main function that processes the job.
    RunPod passes the 'job' dictionary to this function.
    """
    global MODEL
    
    # 1. Initialize the model if it hasn't been loaded yet
    if MODEL is None:
        MODEL = load_model()

    # 2. Extract inputs
    # The actual data sent by the user is inside job['input']
    job_input = job.get("input", {})
    
    # Validate input (Optional but recommended)
    if not job_input:
        return {"error": "No input provided"}

    print(f"Processing job {job.get('id')} with input: {job_input}")

    # 3. Run Inference
    try:
        # ------------------------------------------------------------------
        # REPLACE THIS BLOCK WITH YOUR ACTUAL INFERENCE LOGIC
        # prompt = job_input.get("prompt", "Default prompt")
        # result = MODEL(prompt)
        # ------------------------------------------------------------------
        
        # Simulating processing
        prompt = job_input.get("prompt", "Hello World")
        result = f"Generated output for: {prompt} using {MODEL}"
        
        # 4. Return the output
        # You can return a dictionary, string, or list.
        return {
            "result": result,
            "status": "success"
        }

    except Exception as e:
        print(f"Error processing job: {e}")
        return {"error": str(e)}

# --- Entrypoint ---
# This starts the RunPod serverless worker.
if __name__ == "__main__":
    # Optional: Load the model immediately upon container start
    # This increases startup time but ensures the first request is fast.
    # MODEL = load_model() 
    
    print("Starting RunPod Serverless Worker...")
    runpod.serverless.start({"handler": handler})
