from markets.models import Market


def update_markets_volumes_prices():
    for market in Market.objects.all():
        if market.base.code != 'BTC' and market.coin.code != 'BTC':
            market.price_btc = market.price * market.base.price_btc
            market.volume_btc = market.volume * market.base.price_btc

        if market.base.code not in ('USD', 'USDT') and market.coin.code not in ('USD', 'USDT'):
            market.price_usd = market.price * market.base.price_usd
            market.volume_usd = market.volume * market.base.price_usd

        market.save()


def update_base_volumes(market):
    if market.base.code == 'BTC':
        market.price_btc = market.price
        market.volume_btc = market.volume
    elif market.coin.code == 'BTC':
        market.price_btc = 1
        market.volume_btc = market.volume / market.price

    if market.base.code == 'USD' or market.base.code == 'USDT':
        market.volume_usd = market.volume
        market.price_usd = market.price
    elif market.coin.code == 'USD' or market.coin.code == 'USDT':
        market.price_usd = 1
        market.volume_usd = market.volume / market.price

    market.save()
