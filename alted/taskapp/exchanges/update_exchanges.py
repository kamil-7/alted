from django.db.models import Sum

from exchanges.models import Exchange


def update_exchanges():
    for exchange in Exchange.objects.all():
        exchange.volume_usd = exchange.market_set.all().aggregate(Sum('volume_usd'))['volume_usd__sum']
        exchange.volume_btc = exchange.market_set.all().aggregate(Sum('volume_btc'))['volume_btc__sum']
        exchange.save()
