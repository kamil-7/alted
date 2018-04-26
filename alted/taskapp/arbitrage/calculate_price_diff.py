from arbitrage.models import PriceDiffPair, PriceDiffTick
from coins.models import Coin


def calculate_price_diff():
    for price_diff_pair in PriceDiffPair.objects.all():
        market = price_diff_pair.market
        pln = Coin.objects.get(code='PLN')
        # import IPython.core.debugger; IPython.core.debugger.set_trace()
        buy = (price_diff_pair.market.lowest_ask * pln.price_usd / price_diff_pair.base_coin.price_usd - 1) * 100
        sell = (price_diff_pair.market.highest_bid * pln.price_usd / price_diff_pair.base_coin.price_usd - 1) * 100

        PriceDiffTick.objects.create(
            pair=price_diff_pair,
            buy=buy,
            buy_price=market.lowest_ask,
            sell=sell,
            sell_price=market.highest_bid,
        )
