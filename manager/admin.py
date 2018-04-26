from django.contrib import admin

from manager.models import PreCoin


@admin.register(PreCoin)
class PreCoinAdmin(admin.ModelAdmin):
    pass
