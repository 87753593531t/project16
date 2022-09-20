from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from users.models import CustomUser
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()