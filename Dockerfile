FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

WORKDIR /app/src

# Run app.py when the container launches
ENTRYPOINT ["python", "main_runner.py"]
