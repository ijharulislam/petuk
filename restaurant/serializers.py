from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    images = RestaurantImageSerializer()

    class Meta:
        model = Restaurant
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer()

    class Meta:
        model = Item
        fields = '__all__'


class ItemReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReview
        fields = '__all__'