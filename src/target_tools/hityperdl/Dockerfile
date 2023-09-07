# Pull the Python base image
FROM ghcr.io/saltudelft/type4py:latest

COPY requirements.txt /app/requirements.txt
COPY src /tmp/src

# Install Python dependencies
RUN pip install --upgrade pip
#RUN pip install .
RUN pip install -r /app/requirements.txt

WORKDIR /app

# Clone the repository
RUN git clone https://github.com/JohnnyPeng18/HiTyper.git
COPY patches/config.py /app/HiTyper/hityper/config.py
COPY patches/__main__.py /app/HiTyper/hityper/__main__.py

# Navigate into the cloned repository
WORKDIR /app/HiTyper

# Install Python dependencies
RUN pip install .

WORKDIR /type4py/type4py/server
