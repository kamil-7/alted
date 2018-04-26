from datetime import datetime
from decimal import Decimal

import requests

from alted.taskapp.markets.update_markets_volumes_prices import update_base_volumes
from exchanges.models import Exchange
from markets.models import Market, Tick


def update_markets():
    update_markets_poloniex()
    update_markets_bitfinex()
    update_markets_in('BITM', 'https://www.bitmarket.pl/json/{}{}/ticker.json')
    update_markets_in('BITMS', 'https://bitmaszyna.pl/api/{}{}/ticker.json', key_volume='volume1')
    update_markets_in('BITB', 'https://bitbay.net/API/Public/{}{}/ticker.json')


def update_markets_poloniex():
    poloniex_exchange = Exchange.objects.get(code='PLNX')
    ticker = requests.get('https://poloniex.com/public?command=returnTicker').json()

    for market in Market.objects.filter(exchange=poloniex_exchange).all():
        key = '{}_{}'.format(market.base.code, market.coin.code)
        data = ticker[key]

        market.price = Decimal(data['last'])
        market.volume = Decimal(data['baseVolume'])
        market.highest_bid = Decimal(data['highestBid'])
        market.lowest_ask = Decimal(data['lowestAsk'])

        # Tick.objects.create(market=market, price=market.price)

        update_base_volumes(market)


def update_markets_bitfinex():
    bitfinex_exchange = Exchange.objects.get(code='BTFX')
    code_substitutes = bitfinex_exchange.code_substitutes

    ticker = requests.get(bitfinex_exchange.ticker_url).json()
    ticker = {item[0]: item[1:] for item in ticker}

    for market in Market.objects.filter(exchange=bitfinex_exchange).all():
        coin_code = code_substitutes.get(market.coin.code, market.coin.code)
        key = 't{}{}'.format(coin_code, market.base.code)

        try:
            data = ticker[key]
        except KeyError:
            if not market.crashed:
                market.crashed = datetime.now()
                market.save()
        else:
            market.price = Decimal(data[6])
            market.volume = Decimal(data[7] * data[6])
            market.highest_bid = Decimal(data[0])
            market.lowest_ask = Decimal(data[2])

            if market.crashed:
                market.crashed = None

            update_base_volumes(market)


def update_markets_in(
    exchange_code,
    ticker_url,
    key_price='last',
    key_volume='volume',
    key_highest_bid='bid',
    key_lowest_ask='ask'
):
    exchange = Exchange.objects.get(code=exchange_code)

    for market in Market.objects.filter(exchange=exchange).all():
        url = ticker_url.format(market.coin.code, market.base.code)
        data = requests.get(url).json()
        market.price = Decimal(data[key_price])
        market.volume = Decimal(data[key_volume])
        market.highest_bid = Decimal(data[key_highest_bid])
        market.lowest_ask = Decimal(data[key_lowest_ask])

        update_base_volumes(market)
