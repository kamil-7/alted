from arbitrage.models import PriceDiffPair
from markets.models import Market


def initialize_admin():
    for market in Market.objects.filter(exchange__code__in=['BITM', 'BITB', 'BITMS']):
        PriceDiffPair.objects.create(base_coin=market.coin, market=market)

