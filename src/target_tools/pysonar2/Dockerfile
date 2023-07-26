# Pull the Python base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get -y install git gcc\
    && apt-get -y install default-jdk maven


# Clone the repository
RUN git clone https://github.com/yinwang0/pysonar2.git

# Navigate into the cloned repository
WORKDIR /app/pysonar2

COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN mvn package -DskipTests || true

COPY src /tmp/src
# Set the default command to run when the container starts
CMD ["bash"]
