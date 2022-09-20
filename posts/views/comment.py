from django.http import HttpResponseRedirect
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from posts.models import Comment
from posts.serializers import CommentSerializer, CommentCreateSerializer, CommentUpdateSerializer, CommentListSerializer
from posts.permissions import PostOwnerOrReadOnly


class CommentViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        serializer_class = CommentSerializer

        if self.action == 'create':
            serializer_class = CommentCreateSerializer
        elif self.action == 'update':
            serializer_class =CommentUpdateSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = CommentListSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # serializer_data = CommentSerializer(instance).data
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many = True)
        return Response(serializer.data)


    def get_object(self):
        uuid = self.kwargs['pk']

        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise HttpResponseRedirect

    def get_permissions(self):
        permission_classes = [AllowAny, ]

        if self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAuthenticated, ]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes.append(PostOwnerOrReadOnly)

        return [permission() for permission in permission_classes]