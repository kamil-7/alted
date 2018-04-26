from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.views import APIView

from coins.serializers import CoinSerializer
from markets.serializers import MarketSerializer


class TargetListAPI(APIView):

    def get(self, request):
        target = ContentType.objects.get(id=request.GET.get('target'))
        query = request.GET.get('q', '')
        data = target.model_class().objects.filter(name__icontains=query)

        if target.app_label == 'coins' and target.model == 'coin':
            data = CoinSerializer(data, many=True)
        elif target.app_label == 'markets' and target.model == 'market':
            data = MarketSerializer(data, many=True)

        return Response(data.data)
