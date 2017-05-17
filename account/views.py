from rest_framework import serializers, generics
from .models import User
from .serializers import UserRegistrationSerializer
from .permissions import IsAuthenticatedOrCreate


class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (IsAuthenticatedOrCreate,)