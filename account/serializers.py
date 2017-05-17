from rest_framework.serializers import ModelSerializer, Serializer, ValidationError
from .models import User


class UserRegistrationSerializer(ModelSerializer):

    def create(self, validated_data):
        password = validated_data['password']
        validated_data['is_active'] = True
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'full_name',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }