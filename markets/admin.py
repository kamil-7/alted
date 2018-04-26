from django.contrib import admin

from markets.models import Market, Tick


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'price', 'created', 'crashed', 'price_btc', 'price_usd']
    list_filter = ['crashed', 'exchange']


@admin.register(Tick)
class TickAdmin(admin.ModelAdmin):
    pass
