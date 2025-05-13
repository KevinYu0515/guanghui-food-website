# 記得需要產生 firbase secert，並將檔名改成 serviceAccountKey.json

FROM python:3.10-slim

RUN apt-get update && apt-get install cron -y

WORKDIR /app

COPY . /app

RUN mv cronjob /etc/cron.d/cronjob

RUN chmod 0644 /etc/cron.d/cronjob && crontab /etc/cron.d/cronjob

RUN touch /var/log/cron.log

RUN pip install --no-cache-dir -r requirements.txt

CMD ["cron", "-f"]
