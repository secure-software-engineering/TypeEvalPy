# Pull the Python base image
FROM python:3.10.14-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install gcc python3-packaging

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install -r requirements.txt

COPY src /tmp/src

# Keep the container alive
CMD ["bash"]
