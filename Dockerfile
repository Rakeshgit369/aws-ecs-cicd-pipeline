FROM python:3.9-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

ENV PYTHONUNBUFFERED=1

COPY requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

CMD ["python","-m", "src.main"]