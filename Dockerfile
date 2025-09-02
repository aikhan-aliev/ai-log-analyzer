FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY src/ ./src
COPY logs/ ./logs
COPY reports/ ./reports

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "src/main.py"]
