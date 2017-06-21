from rest_framework.serializers import ModelSerializer
from .models import Offer
from restaurant.serializers import RestaurantSerializer, ItemSerializer


class OfferSerializer(ModelSerializer):
    offers = RestaurantSerializer(read_only=True, many=True)
    item_offers = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Offer
        fields = '__all__'
        depth = 1
