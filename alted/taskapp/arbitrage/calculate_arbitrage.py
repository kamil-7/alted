from arbitrage.models import ArbitragePair, ArbitrageLog


def calculate_arbitrage():
    for arbitrage_pair in ArbitragePair.objects.filter(active=True):
        for sell_market in arbitrage_pair.markets.order_by('-highest_bid'):
            for buy_market in arbitrage_pair.markets.exclude(id=sell_market.id).order_by('lowest_ask'):

                if buy_market.lowest_ask < sell_market.highest_bid:
                    ArbitrageLog.objects.create(
                        pair=arbitrage_pair,
                        difference=sell_market.highest_bid - buy_market.lowest_ask,
                        difference_percentage=(sell_market.highest_bid / buy_market.lowest_ask - 1) * 100,
                        buy_market=buy_market,
                        sell_market=sell_market
                    )
                else:
                    break

    ArbitrageLog.objects.filter(active=True).delete()
    ArbitrageLog.objects.update(active=True)
