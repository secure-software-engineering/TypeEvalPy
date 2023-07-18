# Pull the Python base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install git gcc

RUN git clone https://github.com/utopia-group/TypeT5.git /app/TypeT5

WORKDIR /app/TypeT5


RUN pip install -r requirements.txt
RUN pip install .


# Run the application
CMD ["bash"]
