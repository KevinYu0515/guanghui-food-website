# 記得需要產生 firbase secert，並將檔名改成 serviceAccountKey.json

FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "catch_news.py"]
