import json

import requests
from django.views.generic import TemplateView


class ChartView(TemplateView):
    template_name = 'pages/chart.html'

    #
    # def get_context_data(self, **kwargs):
    # 	import time
    # 	context = super(ChartView, self).get_context_data(**kwargs)
    # 	data = list()
    #
    # 	okcoin_raw_data = requests.get('https://www.okcoin.cn/api/v1/kline.do?symbol=btc_cny&type=1min').json()
    # 	okcoin_data = list()
    # 	for tick in okcoin_raw_data:
    # 		print(tick)
    # 		okcoin_data.append([tick[0], tick[4]])
    #
    # 	time.sleep(1)
    #
    # 	eth_raw_data = requests.get('https://www.okcoin.cn/api/v1/kline.do?symbol=eth_cny&type=1min').json()
    # 	eth_data = list()
    # 	for index, tick in enumerate(eth_raw_data):
    # 		print(tick)
    # 		price = tick[4] / okcoin_data[index][1]
    # 		eth_data.append([tick[0], price])
    # 	data.append(eth_data)
    #
    # 	time = int(time.time()) - 60 * 1000
    # 	polo_raw_data = requests.get('https://api.cryptowat.ch/markets/poloniex/ethbtc/ohlc?periods=60&after={}'.format(time)).json()['result']['60']
    # 	polo_data = list()
    # 	print('len cryptowatch data', len(okcoin_data))
    #
    # 	for tick in polo_raw_data:
    # 		polo_data.append([tick[0] * 1000, tick[4]])
    # 	data.append(polo_data)
    #
    # 	context["data"] = json.dumps(data)
    #
    # 	return context
    #

    def get_context_data(self, **kwargs):
        import time
        context = super(ChartView, self).get_context_data(**kwargs)
        data = list()

        okcoin_raw_data = requests.get('https://www.okcoin.cn/api/v1/kline.do?symbol=btc_cny&type=1min').json()
        okcoin_data = list()
        for tick in okcoin_raw_data:
            print(tick)
            okcoin_data.append([tick[0], tick[4]])

        chbtc_raw_data = requests.get('http://api.chbtc.com/data/v1/kline?currency=bts_cny&type=1min').json()['data']
        chbtc_data = list()
        for index, tick in enumerate(chbtc_raw_data):
            price = tick[4] / okcoin_data[index][1]
            chbtc_data.append([tick[0], price])
        data.append(chbtc_data)

        time = int(time.time()) - 60 * 1000
        polo_raw_data = \
            requests.get(
                'https://api.cryptowat.ch/markets/poloniex/btsbtc/ohlc?periods=60&after={}'.format(time)).json()[
                'result']['60']
        polo_data = list()
        print('len cryptowatch data', len(okcoin_data))

        for tick in polo_raw_data:
            polo_data.append([tick[0] * 1000, tick[4]])
        data.append(polo_data)

        context["data"] = json.dumps(data)

        return context
