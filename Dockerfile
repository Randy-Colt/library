FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./src .