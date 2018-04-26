from django.contrib import admin

from exchanges.models import Exchange


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass
