from rest_framework.serializers import ModelSerializer, Serializer, ValidationError
from .models import User


class UserRegistrationSerializer(ModelSerializer):

    def validate(self, data):
        password = self.initial_data['password']
        confirm_password = self.initial_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('Password does not match!')
        return data

    def create(self, validated_data):
        password = validated_data['password']
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }