import json

from django.views.generic import DetailView
from django.views.generic import ListView

from alted.utils import CustomEncoder
from markets.models import Market, Tick
from markets.serializers import MarketSerializer


class MarketListView(ListView):
    queryset = Market.objects.all().order_by('-volume_btc')
    template_name = 'pages/markets/market_list/market_list.html'


class MarketDetailView(DetailView):
    model = Market
    template_name = 'pages/markets/market_detail/market_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MarketDetailView, self).get_context_data(**kwargs)
        market = context['object']

        context['data'] = json.dumps(dict(
            chart=list(Tick.objects.values_list('date', 'price')),
            market=MarketSerializer(market).data,
        ), cls=CustomEncoder)

        return context
