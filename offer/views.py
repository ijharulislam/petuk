from common.viewsets import BaseModelViewSet

from .models import Offer
from .serializers import OfferSerializer


class OfferViewSet(BaseModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
