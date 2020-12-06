from .serializers import UserSerializer
# Create your views here.
from .models import CustomUser
from rest_framework import generics

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

