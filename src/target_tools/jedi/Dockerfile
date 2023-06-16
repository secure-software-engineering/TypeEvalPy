# Pull the Python base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install gcc \
    && apt-get -y install watchman \
    && apt-get -y install jq

COPY requirements.txt /app/requirements.txt
COPY jedi_type_inference.py /tmp/jedi_type_inference.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the application
CMD ["bash"]
