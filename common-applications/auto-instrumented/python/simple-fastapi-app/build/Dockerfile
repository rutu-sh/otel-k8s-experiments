FROM python:3.9-slim

ENV PYTHONPATH="/app/src:${PYTHONPATH}"

WORKDIR /app

COPY requirements.txt . 

RUN pip3 install -r requirements.txt

WORKDIR /app/src

COPY src .

CMD "opentelemetry-instrument" "python3" "main.py"