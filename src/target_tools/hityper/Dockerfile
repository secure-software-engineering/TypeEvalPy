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
COPY patches/__main__.py /app/HiTyper/hityper/__main__.py

# Navigate into the cloned repository
WORKDIR /app/HiTyper

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install .

RUN pip install PyCG==0.0.4

COPY src /tmp/src

# Set the default command to run when the container starts
CMD ["bash"]
