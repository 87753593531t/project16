from rest_framework import serializers




from posts.models import Post
from users.serializers import UserSerializer
# from .comment import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'uuid',
            'title',
            'text',
            'kind',
            'author',
            'like'
            # 'comment'

        )


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'uuid',
            'title',
            'text',
            'kind',
            'author',
            'like',
            # 'comment'



        )


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Post
        field = (
            # 'comment',
            'author',
            'like',

        )


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        field = (
            # 'comment',
            'author',
            'like',

        )

    def update(self, instance, validated_data):
        if 'author' in validated_data.keys():
            author = Post.objects.filter(id=instance.author_id).first()
            author_serializer = PostCreateSerializer(author)
            author_serializer.update(author, dict(validated_data['author']))
            del validated_data['author']
        return super().update(instance, validated_data)



