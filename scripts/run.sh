#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module ckintai_kun.wsgi --uid 1000 --gid 1000