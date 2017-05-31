from common.viewsets import BaseModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import *
from .serializers import *


class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RestaurantViewSet(BaseModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @list_route(methods=['GET'])
    def nearest(self, request):
        lat = float(request.query_params.get('lat', 23.8103))
        lon = float(request.query_params.get('lon', 90.4125))
        points = 5 * .008
        restaurants = Restaurant.objects.filter(
            lat__gte=lat - points,
            lat__lte=lat + points,
            lon__gte=lon - points,
            lon__lte=lon + points,
        )
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


class RestaurantImageViewSet(BaseModelViewSet):
    queryset = RestaurantImage.objects.all()
    serializer_class = RestaurantImageSerializer


class ReviewViewSet(BaseModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ItemViewSet(BaseModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

