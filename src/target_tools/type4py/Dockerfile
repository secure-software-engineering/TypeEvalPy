# Pull the Python base image
FROM ghcr.io/saltudelft/type4py:latest

COPY requirements.txt /app/requirements.txt
COPY src /tmp/src

# Install Python dependencies
RUN pip install --upgrade pip
#RUN pip install .
RUN pip install -r /app/requirements.txt
