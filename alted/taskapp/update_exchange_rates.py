import requests

from coins.models import Coin

APILAYER_KEY = '915d6bc9acb45a205941701a6dde9637'


def update_exchange_rates():
    data = requests.get('http://www.apilayer.net/api/live?access_key={}&format=0'.format(APILAYER_KEY)).json()['quotes']

    for coin in Coin.foreign_fiats.all():
        coin.price_usd = 1 / data['USD' + coin.code]
        coin.save()
