# Use a RunPod-compatible base image
FROM runpod/base:0.4.0-cuda11.8.0

# Set working directory to root
WORKDIR /

# 1. Install Dependencies
# Copy requirements first to leverage Docker caching
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 2. Copy Application Code
# This copies handler.py (and everything else) to /
COPY . .

# 3. Run the Handler
# -u is CRITICAL: It forces unbuffered stdout, so you see logs in real-time.
# We use the exact filename 'handler.py' copied above.
CMD [ "python3", "-u", "handler.py" ]
