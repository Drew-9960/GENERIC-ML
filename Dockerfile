FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app
COPY requirements.txt /app/requirements.txt

RUN apt update -y && apt install -y awscli python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
