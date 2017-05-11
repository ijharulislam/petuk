from common.viewsets import BaseModelViewSet, ReadOnlyModelViewSet

from .models import *
from .serializers import *


class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RestaurantViewSet(BaseModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantImageViewSet(BaseModelViewSet):
    queryset = RestaurantImage.objects.all()
    serializer_class = RestaurantImageSerializer


class ReviewViewSet(BaseModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ItemViewSet(BaseModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

