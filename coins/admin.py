from django.contrib import admin

from coins.models import Coin


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Coin._meta.fields if field.name != "id"]
