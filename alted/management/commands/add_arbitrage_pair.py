import itertools
from django.core.management import BaseCommand

from arbitrage.models import ArbitragePair
from coins.models import Coin
from markets.models import Market


class Command(BaseCommand):

    def handle(self, *args, **options):
        # buy_coin = input('Input base coin code')
        # sell_coin = input('Input proxy coin code')
        #
        # buy_coin = Coin.objects.get(code=buy_coin)
        # sell_coin = Coin.objects.get(code=sell_coin)
        #
        #

        for market in Market.objects.all():
            arbitrage_pair, created = ArbitragePair.objects.get_or_create(coin=market.coin, base=market.base)
            arbitrage_pair.markets.add(market)

        for arbitrage_pair in ArbitragePair.objects.all():
            if arbitrage_pair.markets.count() < 2:
                arbitrage_pair.delete()
