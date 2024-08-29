# Pull the Python base image
FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CUDA_HOME=/usr/local/cuda
ENV PATH=/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}
# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install gcc python3-packaging python3-pip python3-dev python3-venv python3-setuptools git

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install setuptools 
RUN pip install torch==2.1.2 torchvision==0.16.2
RUN pip install -r requirements.txt
RUN pip install flash-attn

RUN ln -s /usr/bin/python3 /usr/bin/python


COPY src /tmp/src

# Keep the container alive
CMD ["bash"]
