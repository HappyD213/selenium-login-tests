FROM python:3.14.2-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y wget && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest"]