import runpod
import os

# --- Load your model/globals here (Warm Start) ---
# This runs once when the container starts.
# MODEL = load_my_model()

def handler(job):
    """
    The handler function that RunPod calls for every job.
    Signature: Must take a 'job' dictionary argument.
    """
    # 1. Extract Input
    job_input = job["input"]
    
    # 2. Process the job
    # (Replace this with your actual model inference)
    # result = MODEL.predict(job_input)
    print(f"Processing job {job.get('id')} with input: {job_input}")
    
    result = {"message": "Job processed successfully", "input_received": job_input}

    # 3. Return output
    return result

# --- Entrypoint ---
# According to your docs: "runpod.serverless.start call must be present... 
# not hidden behind conditions other than the usual if __name__ == '__main__':"
if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
