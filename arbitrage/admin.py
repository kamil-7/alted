from django.contrib import admin

from arbitrage.models import ArbitragePair, ArbitrageLog, PriceDiffPair, PriceDiffTick


@admin.register(ArbitragePair)
class ArbitragePairAdmin(admin.ModelAdmin):
    pass


@admin.register(ArbitrageLog)
class ArbitrageLogAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceDiffTick)
class PriceDiffTickAdmin(admin.ModelAdmin):
    list_display = ['pair', 'date']


@admin.register(PriceDiffPair)
class PriceDiffPairAdmin(admin.ModelAdmin):
    pass
