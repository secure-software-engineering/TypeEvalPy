# Pull the Python base image
FROM gradle:8.2.1-jdk17

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install gcc git

RUN git clone https://github.com/JetBrains-Research/psiminer.git

RUN ./gradlew build

COPY src /tmp/src

# Keep the container alive
CMD ["bash"]
