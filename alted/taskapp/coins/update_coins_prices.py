from alted.taskapp.coins.tick_coin_price import tick_coin_price
from coins.models import Coin


def update_coins_prices(usd_coin, btc_coin, btc_usd_market, usdt_coin):
    btc_coin.price_usd = btc_coin.market_set.filter(base=usd_coin).order_by('-volume').first().price
    btc_coin.price_btc = 1
    tick_coin_price(btc_coin)
    btc_coin.save()

    usd_coin.price_usd = 1
    usd_coin.price_btc = 1 / btc_coin.price_usd
    tick_coin_price(usd_coin)
    usd_coin.save()

    usdt_coin.price_usd = 1
    usdt_coin.price_btc = usd_coin.price_btc
    tick_coin_price(usdt_coin)
    usdt_coin.save()

    for coin in Coin.objects.filter(fiat=False).exclude(code='BTC'):
        update_coin_price(coin, btc_coin, btc_usd_market)

    for coin in Coin.foreign_fiats.all():
        update_fiat_price(coin, btc_coin)


def update_coin_price(coin, btc_coin, btc_usd_market):
    markets = coin.market_set

    top_market = markets.filter(base=btc_coin).first()

    if top_market:
        coin.price_btc = top_market.price
        coin.price_usd = top_market.price * btc_usd_market.price
    else:
        top_market = coin.base_market_set.filter(coin=btc_coin).order_by('-volume_btc').first()
        if not top_market:
            raise Exception('Coin {} has no market'.format(coin.code))

        coin.price_btc = 1 / top_market.price
        coin.price_usd = coin.price_btc * btc_usd_market.price

    tick_coin_price(coin)
    coin.save()


def update_fiat_price(coin, btc_coin):
    top_market = coin.base_market_set.filter(coin=btc_coin).order_by('-volume').first()
    coin.price_btc = 1 / top_market.price

    tick_coin_price(coin)
    coin.save()
