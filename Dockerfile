# Use the official RunPod base image. 
# This includes Python 3.10, CUDA 11.8, and common ML libraries.
# You can change the tag to '0.6.2-cuda12.2.0' if you need newer CUDA.
FROM runpod/base:0.4.0-cuda11.8.0

# Set the working directory to the root of the container
WORKDIR /

# Add necessary files
ADD handler.py ./

# pip install
ADD requirements.txt ./
RUN pip install -r requirements.txt

# --- Application Code ---
# Copy all files from your current directory into the container
COPY . .

# --- Entrypoint ---
# This command runs your handler script.
# IMPORTANT: Replace 'handler.py' with the actual name of your main python script.
CMD [ "python", "-u", "handler.py" ]
