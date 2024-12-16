FROM python:3.10-slim

WORKDIR /app

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

WORKDIR /app/src

CMD [ "python main.py" ]

EXPOSE 8000