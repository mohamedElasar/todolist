from rest_framework import generics
from users.serializers import UserSerializer
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
