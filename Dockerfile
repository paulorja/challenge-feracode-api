FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /diapers

WORKDIR /diapers

ADD . /diapers

RUN pip install -r requirements.txt
