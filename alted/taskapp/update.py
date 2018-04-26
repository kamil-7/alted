from celery.task import task

from alted.taskapp.arbitrage.calculate_arbitrage import calculate_arbitrage
from alted.taskapp.arbitrage.calculate_price_diff import calculate_price_diff
from alted.taskapp.coins.update_coins_prices import update_coins_prices
from alted.taskapp.coins.update_coins_volumes import update_coins_volumes
from alted.taskapp.exchanges.update_exchanges import update_exchanges
from alted.taskapp.markets.update_markets import update_markets

from alted.taskapp.markets.update_markets_volumes_prices import update_markets_volumes_prices
from alted.taskapp.signals.check_signals import check_signals
from coins.models import Coin
from markets.models import Market


@task
def update():
    # often used objects
    btc_coin = Coin.objects.get(code='BTC')
    usd_coin = Coin.objects.get(code='USD')
    btc_usd_market = Market.objects.filter(base=usd_coin, coin=btc_coin).order_by('-volume_btc').first()
    usdt_coin = Coin.objects.get(code='USDT')

    # api fetch
    update_markets()

    # post-fetch
    update_coins_prices(usd_coin, btc_coin, btc_usd_market, usdt_coin)
    update_markets_volumes_prices()
    update_coins_volumes()
    update_exchanges()

    calculate_arbitrage()
    calculate_price_diff()

    check_signals()
