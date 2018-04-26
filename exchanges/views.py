from django.views.generic import DetailView
from django.views.generic import ListView

from exchanges.models import Exchange


class ExchangeListView(ListView):
    queryset = Exchange.objects.all().order_by('-volume_btc')
    template_name = 'pages/exchanges/exchange_list/exchange_list.html'


class ExchangeDetailView(DetailView):
    model = Exchange
    template_name = 'pages/exchanges/exchange_detail/exchange_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExchangeDetailView, self).get_context_data(**kwargs)
        exchange = context['object']
        context['market_list'] = exchange.market_set.all()

        return context
