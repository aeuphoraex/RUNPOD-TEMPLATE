import runpod

def handler(job):
    """
    The handler function is the entry point for the worker.
    It receives the 'job' dictionary which contains the input.
    """
    # 1. Extract input data
    job_input = job['input']
    
    # --- YOUR CUSTOM LOGIC GOES HERE ---
    # Example: Get a 'name' from input, default to 'World'
    name = job_input.get("name", "World")
    
    # Example logic: just returning a string
    result = f"Hello, {name}!"
    
    # 2. Return the output
    return result

# 3. Start the worker
if __name__ == '__main__':
    # This keeps the script running, listening for jobs from RunPod
    runpod.serverless.start({"handler": handler})
