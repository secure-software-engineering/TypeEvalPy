# Pull the Python base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get -y install git gcc

# Clone the repository
RUN git clone https://github.com/JohnnyPeng18/HiTyper.git

# Navigate into the cloned repository
WORKDIR /app/HiTyper

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install .

# Set the default command to run when the container starts
CMD ["bash"]
