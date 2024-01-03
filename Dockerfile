FROM python:alpine

WORKDIR app

ADD requirements.txt .

RUN pip install -r requirements.txt && rm requirements.txt

ADD bot.py .

ENTRYPOINT python bot.py
