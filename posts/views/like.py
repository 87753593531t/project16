from rest_framework import status, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from collections import Counter
from itertools import groupby
from django_filters import rest_framework as filters
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from posts.models import PostLike
from posts.serializers import PostLikeSerializer, PostLikeListSerializer, PostLikeUpdateSerializer
from posts.permissions import PostLikeOwnerOrReadOnly





class PostLikeViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': self.request, 'kwargs': kwargs})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = PostLikeListSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'add_like' or self.action == 'add_dislike':
            serializer_class = PostLikeSerializer

        return serializer_class

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ]

        if self.action == 'retrieve' or self.action == 'create':
            permission_classes = [PostLikeOwnerOrReadOnly, ]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes.append(PostLikeOwnerOrReadOnly)
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser, ]

        return [permission() for permission in permission_classes]



    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def add_like(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request,
                                                                     'kwargs': kwargs})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
