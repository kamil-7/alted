from rest_framework import serializers

from coins.models import Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'name', 'slug', 'price_btc', 'price_usd', 'volume_btc', 'volume_usd')
