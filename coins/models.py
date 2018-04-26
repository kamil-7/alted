from django.db import models

from alted.utils import SlugifyMixin
from markets.models import Market

CALCULATION_CHOICES = (
    (0, 'signal / base'),
    (1, 'signal / (base / proxy)'),
    (2, '(signal / proxy) / base')
)


class CoinManager(models.Manager):
    def get_queryset(self):
        queryset = super(CoinManager, self).get_queryset()
        return queryset.filter(fiat=True, tethered_fiat=None).exclude(code='USD')


class Coin(models.Model, SlugifyMixin):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=8, unique=True)
    fiat = models.BooleanField(default=False)

    slug = models.SlugField(max_length=32, unique=True, blank=True)

    price_usd = models.DecimalField(max_digits=16, decimal_places=8, null=True, blank=True)
    price_btc = models.DecimalField(max_digits=16, decimal_places=8, null=True, blank=True)
    volume_usd = models.DecimalField(max_digits=32, decimal_places=2, null=True, blank=True)
    volume_btc = models.DecimalField(max_digits=32, decimal_places=8, null=True, blank=True)

    tethered_fiat = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()
    foreign_fiats = CoinManager()

    def __str__(self):
        return self.code

    def save(self, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        super(Coin, self).save(**kwargs)


class Tick(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    price_usd = models.DecimalField(max_digits=32, decimal_places=8)
    price_btc = models.DecimalField(max_digits=32, decimal_places=8)
