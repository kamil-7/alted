from django.db import models

from alted.utils import SlugifyMixin
from exchanges.models import Exchange


class Market(models.Model, SlugifyMixin):
    name = models.CharField(max_length=48, blank=True, unique=True)
    slug = models.SlugField(max_length=48, blank=True, unique=True)

    coin = models.ForeignKey('coins.Coin', on_delete=models.CASCADE)
    base = models.ForeignKey('coins.Coin', related_name='base_market_set', on_delete=models.CASCADE)
    exchange = models.ForeignKey('exchanges.Exchange', on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)

    volume = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)

    price_usd = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)
    price_btc = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)

    volume_usd = models.DecimalField(max_digits=32, decimal_places=2, default=0, blank=True)
    volume_btc = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)

    day_high = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)
    day_low = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)

    highest_bid = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)
    lowest_ask = models.DecimalField(max_digits=32, decimal_places=8, default=0, blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True)
    crashed = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('exchange', 'coin', 'base')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = '{}/{} {}'.format(self.coin.code, self.base.code, self.exchange.name)
        if not self.slug:
            self.slug = self.get_unique_slug()
        super(Market, self).save(*args, **kwargs)


class Tick(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=16, decimal_places=8)
