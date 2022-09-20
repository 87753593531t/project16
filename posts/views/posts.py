from django.http import Http404
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from collections import Counter
from itertools import groupby
from rest_framework import generics

from posts.models import Post,PostLike
from posts.serializers import PostSerializer, PostListSerializer, PostLikeSerializer, PostLikeListSerializer
from posts.filters import PostLikeFilter


class PostViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = PostListSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def get_object(self):
        uuid = self.kwargs['pk']

        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise Http404



class AnaliticViewSet(generics.ListAPIView):
    """список"""

    queryset = PostLike.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostLikeFilter
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated, ]


    def get(self, request, format=None):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        ordered_queryset = filtered_queryset.order_by('updated_at')
        likes_by_updated_at = groupby(ordered_queryset, lambda like: like.updated_at.strftime('%Y-%m-%d'))

        response = []
        for updated_at, likes in likes_by_updated_at:
            count = Counter(like.like for like in likes)
            response.append(
                {
                    'updated_at': updated_at,
                    'Likes': count['LIKE'],
                    'Dislikes': count['DISLIKE'],

                }
            )

        return Response(data=response, status=status.HTTP_200_OK)



