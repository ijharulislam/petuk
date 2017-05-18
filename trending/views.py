from common.viewsets import BaseModelViewSet

from .models import Trending
from .serializers import TrendingSerializer


class TrendingViewSet(BaseModelViewSet):
    queryset = Trending.objects.all()
    serializer_class = TrendingSerializer
