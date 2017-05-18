from rest_framework.serializers import ModelSerializer
from .models import Trending


class TrendingSerializer(ModelSerializer):
    class Meta:
        model = Trending
        fields = '__all__'
