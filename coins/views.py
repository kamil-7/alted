import json

from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView

from alted.utils import CustomEncoder
from coins.models import Coin, Tick
from coins.serializers import CoinSerializer
from markets.models import Market
from markets.serializers import MarketSerializer


class CoinListView(ListView):
    queryset = Coin.objects.filter(fiat=False).order_by('-volume_btc')
    template_name = 'pages/coins/coin_list/coin_list.html'


class CoinDetailView(DetailView):
    model = Coin
    template_name = 'pages/coins/coin_detail/coin_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CoinDetailView, self).get_context_data(**kwargs)
        coin = context['object']

        context['data'] = json.dumps(dict(
            chart=list(Tick.objects.filter(coin=coin).values_list('date', 'price_usd')),
            coin=CoinSerializer(coin).data,
            markets=MarketSerializer((coin.market_set.all() | coin.base_market_set.all()).order_by('-volume_usd'), many=True).data
        ), cls=CustomEncoder)

        return context


class CoinMarketsView(DetailView):
    model = Coin
    template_name = 'pages/coins/coin_markets/coin_markets.html'

    def get_context_data(self, **kwargs):
        context = super(CoinMarketsView, self).get_context_data(**kwargs)
        coin = context['object']
        market_list = Market.objects.filter(Q(coin=coin) | Q(base=coin)).order_by('-volume_btc')
        context['market_list'] = market_list
        return context


class CoinDetailAPI(RetrieveAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CoinSerializer
    queryset = Coin.objects.all()
    lookup_field = "slug"
