from django.contrib import admin

from signals.models import Signal, Condition, TelegramToken, Event


@admin.register(Signal)
class SignalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Signal._meta.fields if field.name != "id"]


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('user', 'operator', 'value', 'signal')


@admin.register(TelegramToken)
class TelegramTokenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TelegramToken._meta.fields if field.name != "id"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'signal')
