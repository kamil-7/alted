import requests
from celery.task import task

from alted.taskapp.exchanges.update_ticker_url import update_ticker_url
from coins.models import Coin
from exchanges.models import Exchange
from manager.models import PreCoin
from markets.models import Market

FIAT_COINS = ('USD', 'USDT', 'PLN', 'EUR', 'KRW', 'JPY')

MARKETS = (
    ('BITM', (
        ('BTC', 'PLN'),
        ('LTC', 'PLN')
    )),
    ('BITMS', (
        ('BTC', 'PLN'),
        ('LTC', 'PLN')
    )),
    ('BITB', (
        ('BTC', 'PLN'),
        ('LTC', 'PLN')
    ))
)


def fill_coin(code, force_coins):
    coin = None

    try:
        coin = Coin.objects.get(code=code)
    except Coin.DoesNotExist:
        if force_coins:
            coin = Coin.objects.create(code=code, name=code + ' coin', fiat=code in FIAT_COINS)
        else:
            PreCoin.objects.get_or_create(code=code)

    return coin


def add_market(exchange, coin_code, base_code, force_coins):
    try:
        Market.objects.get(
            exchange=exchange,
            base__code=base_code,
            coin__code=coin_code
        )
    except Market.DoesNotExist:
        coin = fill_coin(coin_code, force_coins)
        base = fill_coin(base_code, force_coins)

        if coin and base:
            Market.objects.create(exchange=exchange, coin=coin, base=base)


def update_market_list_poloniex(force_coins):
    poloniex_exchange = Exchange.objects.get(code='PLNX')
    ticker = requests.get('https://poloniex.com/public?command=returnTicker').json()

    for key in ticker:
        base_code = key.split('_')[0]
        coin_code = key.split('_')[1]

        add_market(poloniex_exchange, coin_code, base_code, force_coins)


def update_market_list_bittrex(force_coins):
    bitfinex_exchange = Exchange.objects.get(code='BTFX')
    bitfinex_symbols = requests.get('https://api.bitfinex.com/v1/symbols').json()
    for symbol in bitfinex_symbols:
        base_code = symbol[-3:].upper()
        coin_code = symbol[:-3].upper()

        add_market(bitfinex_exchange, coin_code, base_code, force_coins)


@task
def update_market_list(force_coins=False):
    update_market_list_poloniex(force_coins)
    update_market_list_bittrex(force_coins)
    update_ticker_url()

    for market in MARKETS:
        exchange = Exchange.objects.get(code=market[0])

        for coin, base in market[1]:
            add_market(exchange, coin, base, force_coins)
