# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
ADD . /code/