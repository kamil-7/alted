from django.contrib import admin

from trades.models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Trade._meta.fields if field.name != "id"]
