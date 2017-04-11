from rest_framework import permissions
from rest_framework import viewsets

from .models import MyUser
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrCreate, IsOwnerOrReadOnly)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
