from exchanges.models import Exchange
from markets.models import Market


def update_ticker_url_bitfinex():
    bitfinex_exchange = Exchange.objects.get(code='BTFX')

    url = 'https://api.bitfinex.com/v2/tickers?symbols='

    for market in Market.objects.filter(exchange=bitfinex_exchange).values_list('coin__code', 'base__code'):
        url = '{}t{}{},'.format(url, market[0], market[1])

    bitfinex_exchange.ticker_url = url[:-1]
    bitfinex_exchange.save()


def update_ticker_url():
    update_ticker_url_bitfinex()
