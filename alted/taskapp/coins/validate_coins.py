from celery.task import task

from coins.models import Coin


@task
def validate_coins():
    for coin in Coin.objects.all():
        if not coin.market_set:
            print('Coin {} has no markets'.format(coin.code))
