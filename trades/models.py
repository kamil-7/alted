from django.db import models

from markets.models import Market
from users.models import User

ACTION_CHOICES = (
    (1, 'Buy'),
    (2, 'Sell'),
)


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    action = models.PositiveSmallIntegerField(choices=ACTION_CHOICES)
    price = models.DecimalField(max_digits=14, decimal_places=8)
    amount = models.DecimalField(max_digits=18, decimal_places=8)
    total = models.DecimalField(max_digits=14, decimal_places=8)
    fee = models.DecimalField(max_digits=12, decimal_places=8)
    date = models.DateTimeField()
