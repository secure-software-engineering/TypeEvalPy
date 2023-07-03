# Pull the Python base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install gcc

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src /tmp/src

# Custom patch to fix simple errors
COPY patches/typeinfer.py /usr/local/lib/python3.10/site-packages/scalpel/typeinfer/typeinfer.py

# Run the application
CMD ["bash"]
