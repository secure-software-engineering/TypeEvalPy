# Pull the Python base image
FROM ghcr.io/saltudelft/type4py:latest

COPY requirements.txt /app/requirements.txt
COPY src /tmp/src
COPY micro-benchmark/python_features /tmp/micro-benchmark

# Install Python dependencies
RUN pip install --upgrade pip
#RUN pip install .
RUN pip install -r /app/requirements.txt

# Run app.py when the container launches
ENTRYPOINT ["python", "/tmp/src/runner.py"]