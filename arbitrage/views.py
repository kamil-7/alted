import datetime
import json

from django.views.generic import ListView, DetailView

from alted.utils import CustomEncoder
from arbitrage.models import ArbitrageLog, PriceDiffPair, PriceDiffTick


class ArbitrageListView(ListView):
    queryset = ArbitrageLog.objects.filter(active=True)
    template_name = 'pages/arbitrage'


class PriceDiffDetailView(DetailView):
    model = PriceDiffPair
    template_name = 'pages/arbitrage/price_diff_detail/price_diff_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PriceDiffDetailView, self).get_context_data(**kwargs)
        pair = context['object']

        date_from = datetime.datetime.now() - datetime.timedelta(minutes=190)

        context['data'] = json.dumps(dict(
            chart=list(PriceDiffTick.objects.filter(pair=pair, date__gt=date_from).order_by('date').values_list('date', 'buy', 'sell', 'buy_price', 'sell_price')),
        ), cls=CustomEncoder)

        return context


class PriceDiffListView(ListView):
    model = PriceDiffPair
    template_name = 'pages/arbitrage/price_diff_list/price_diff_list.html'
