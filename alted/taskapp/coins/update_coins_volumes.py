from django.db.models import Sum

from coins.models import Coin


def update_coins_volumes():
    for coin in Coin.objects.all():
        markets = coin.market_set
        base_markets = coin.base_market_set

        coin.volume_btc = 0
        coin.volume_usd = 0

        if markets.exists():
            coin.volume_btc += markets.aggregate(Sum('volume_btc'))['volume_btc__sum']
            coin.volume_usd += markets.aggregate(Sum('volume_usd'))['volume_usd__sum']

        if base_markets.exists():
            coin.volume_btc += base_markets.aggregate(Sum('volume_btc'))['volume_btc__sum']
            coin.volume_usd += base_markets.aggregate(Sum('volume_usd'))['volume_usd__sum']

        coin.save()
