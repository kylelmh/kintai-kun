# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/requirements.txt
COPY . /code/
WORKDIR /code
EXPOSE 8000
RUN pip3 install -r requirements.txt && \
    adduser --disabled-password --no-create-home app &&\
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chown -R 755 /vol

USER app

CMD ["run.sh"]