from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

TASKS_FILES = [
    'update',
    'update_market_list',
    'signals.check_signals',
]

app = Celery('alted', include=['alted.taskapp.' + tasks_file for tasks_file in TASKS_FILES])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
