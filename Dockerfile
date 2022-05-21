
# syntax=docker/dockerfile:1
FROM python:3.9-alpine as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/requirements.txt
RUN apk add --update --no-cache --virtual .build-deps \
    build-base \
    postgresql-dev \
    libffi-dev \
    python3-dev \
    libffi-dev \
    jpeg-dev \
    zlib-dev \
    musl-dev \
    libpq
RUN pip3 install -r /code/requirements.txt

FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY ./scripts /scripts
WORKDIR /code
EXPOSE 8000
COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
RUN apk add --update libpq
RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chmod -R +x /scripts && \
    chown -R app:app /code && \
    chown -R app:app /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]