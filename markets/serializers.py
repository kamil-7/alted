from rest_framework import serializers

from markets.models import Market


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'name', 'slug', 'price', 'volume_btc', 'volume_usd')
