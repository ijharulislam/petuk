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

    @list_route(methods=['GET'])
    def featured(self, request):
        restaurants = Restaurant.objects.filter(is_featured=True)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def search(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        query = request.query_params.get('query_param')
        points = 20 * .008
        if lat and lon:
            restaurants = Restaurant.objects.filter(
                lat__gte=lat - points,
                lat__lte=lat + points,
                lon__gte=lon - points,
                lon__lte=lon + points,
            )|Restaurant.objects.filter(name__icontains=query)|\
                Restaurant.objects.filter(address__icontains=query)|\
                Restaurant.objects.filter(address__icontains=query)|\
                Restaurant.objects.filter(tags__icontains=query)|\
                Restaurant.objects.filter(category__name__icontains=query)
        else:
            restaurants = Restaurant.objects.filter(name__icontains=query) | \
            Restaurant.objects.filter(address__icontains=query) | \
            Restaurant.objects.filter(address__icontains=query) | \
            Restaurant.objects.filter(tags__icontains=query) | \
            Restaurant.objects.filter(category__name__icontains=query)
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

