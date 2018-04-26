#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


rm -f './celerybeat.pid'
celery -A alted.taskapp beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
