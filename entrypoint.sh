#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
cat requester.sql | python manage.py dbshell
exec gunicorn mfmk_web_app.wsgi:application --bind 0.0.0.0:8000


