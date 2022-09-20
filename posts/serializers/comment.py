from rest_framework import serializers
# from rest_framework.exceptions import ValidationError

from posts.models import Comment
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = (
            'uuid',
            'post',
            'author',
            'comment'

        )


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = UserSerializer()
    class Meta:
        model = Comment
        fields = (
            'uuid',
            'post',
            'comment',
            'author'
        )


class CommentUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def update(self, instance, validated_data):
        if 'author' in validated_data.keys():
            author = Comment.objects.filter(id=instance.author_id).first()
            author_serializer = CommentCreateSerializer(author)
            author_serializer.update(author, dict(validated_data['author']))
            del validated_data['author']
        return super().update(instance, validated_data)



    class Meta:
        model = Comment
        fields = (
            'uuid',
            'post',
            'comment',
            'author'
        )


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # def validate(self, attrs):
    #
    #
    #         if 'author' in attrs:
    #             new_author_data = attrs['author']
    #             if 'name' not in new_author_data.keys() and \
    #                     'surname' not in new_author_data.keys():
    #                 raise ValidationError('Something wrong with author field info!')
    #
    #             author = Comment.objects.filter(id=self.context['uuid']).first()
    #             if author:
    #                 attrs['author'] = author
    #                 attrs['new_author_data'] = dict(new_author_data)
    #
    #         return attrs


    class Meta:
        model = Comment
        fields = (
            'uuid',
            'post',
            'comment',
            'author'
        )

        read_only_fields = ('created_at', 'updated_at')