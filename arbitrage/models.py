from django.db import models
from django.utils.text import slugify

from coins.models import Coin
from markets.models import Market


#
# class MarketWeb(models.Model):
#     markets = models.ManyToManyField(Market)
#     active = models.BooleanField(default=False)
#
#
# class ArbitrageLog(models.Model):
#     market_web = models.ForeignKey(MarketWeb, on_delete=models.CASCADE)
#     profit = models.DecimalField(max_digits=6, decimal_places=2)
#     date = models.DateTimeField(auto_now_add=True)
#     bought_market = models.ForeignKey(Market, on_delete=models.CASCADE)
#     sold_market = models.ForeignKey(Market, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=14, decimal_places=8)


class ArbitragePair(models.Model):
    base = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='arbitragepair_base_set')
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='arbitragepair_coin_set')
    markets = models.ManyToManyField(Market)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return 'Arbitrage Pair {}/{} | {} markets'.format(self.coin, self.base, self.markets.count())


class ArbitrageLog(models.Model):
    pair = models.ForeignKey(ArbitragePair, on_delete=models.CASCADE)
    difference = models.DecimalField(max_digits=12, decimal_places=8)
    difference_percentage = models.DecimalField(max_digits=12, decimal_places=8)
    buy_market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='arbitragelog_buy_market_set')
    sell_market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='arbitragelog_sell_market_set')
    active = models.BooleanField(default=False)

    def __str__(self):
        return '{} -> {} | {}%'.format(self.buy_market, self.sell_market, self.difference_percentage)


class PriceDiffPair(models.Model):
    slug = models.SlugField(blank=True, null=False)
    base_coin = models.ForeignKey(Coin, blank=True, null=True, on_delete=models.CASCADE)
    base_market = models.ForeignKey(Market, blank=True, null=True, related_name='pricediffpair_base_market_set', on_delete=models.CASCADE)
    market = models.ForeignKey(Market, related_name='pricediffpair_market_set', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.market.slug
        super(PriceDiffPair, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class PriceDiffTick(models.Model):
    pair = models.ForeignKey(PriceDiffPair, on_delete=models.CASCADE)
    buy = models.DecimalField(max_digits=12, decimal_places=8)
    sell = models.DecimalField(max_digits=12, decimal_places=8)
    date = models.DateTimeField(auto_now_add=True)
    buy_price = models.DecimalField(max_digits=32, decimal_places=8)
    sell_price = models.DecimalField(max_digits=32, decimal_places=8)
