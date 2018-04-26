#!/usr/bin/env bash
docker-compose -f local.yml build
docker-compose -f local.yml run django python manage.py makemigrations
docker-compose -f local.yml run django python manage.py migrate
docker-compose -f local.yml run django python manage.py initialize
docker-compose -f local.yml up
