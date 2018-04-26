from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from users.models import User

OPERATOR_CHOICES = (
    (0, 'Equal'),
    (1, 'Higher than'),
    (2, 'Lower than'),
    (3, 'Higher than or equal'),
    (4, 'Lower than or equal'),
)


class TelegramToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    token = models.CharField(max_length=64)


class Signal(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # telegram_token = models.ForeignKey(TelegramToken, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


limit = models.Q(app_label='markets', model='market') | models.Q(app_label='coins', model='coin')


class Condition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signal = models.ForeignKey(Signal, related_name='condition_set', on_delete=models.CASCADE)

    target_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_type', 'target_id')

    operator = models.PositiveSmallIntegerField(choices=OPERATOR_CHOICES)
    value = models.DecimalField(max_digits=32, decimal_places=8)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signal = models.ForeignKey(Signal, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
