from coins.models import Tick


def tick_coin_price(coin):
    Tick.objects.create(
        coin=coin,
        price_btc=coin.price_btc,
        price_usd=coin.price_usd
    )
