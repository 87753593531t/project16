from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from posts.models import Post, PostLike
from posts.serializers import PostCreateSerializer


class PostLikeSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostLike
        fields = (
            'post',
            'author',
            'like',

        )
    def validate(self, attrs):
        pk = attrs['post'].pk
        old = PostLike.objects.filter(uuid=pk)

        author = self.context['request'].user
        old = old.filter(author=author)

        if old:
            raise ValidationError("already done!!!!!")

        # if post:
        #     attrs['post'] = post
        # else:
        #     raise ValidationError('Post not found')
        return attrs

    # def create(self, validated_data):
    #     author = validated_data.pop('author', None)
    #
    #     instance = super().create(validated_data)
    #
    #     if author:
    #         for author_data in author:
    #             author = author_data['uuid']
    #             author.like = instance
    #             author.save(update_fields=['like'])
    #
    #     return instance



class PostLikeListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, attrs):

            if 'author' in attrs:
                new_author_data = attrs['author']
                if 'name' not in new_author_data.keys() and \
                        'surname' not in new_author_data.keys():
                    raise ValidationError('Something wrong with author field info!')

                author = PostLike.objects.filter(id=self.context['uuid']).first()
                if author:
                    attrs['author'] = author
                    attrs['new_author_data'] = dict(new_author_data)

            return attrs
    class Meta:
        model = PostLike
        fields = (
            'post',
            'author',
            'like'
        )


class PostLikeCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostLike
        fields = (
            'post',
            'author',
            'like'
        )

    def create(self, validated_data):
        post = validated_data.pop('author', None)

        instance = super().create(validated_data)

        if post:
            for post_data in post:
                post = post_data['uuid']
                post.like = instance
                post.save(update_fields=['like'])

        return instance


class PostLikeUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostLike
        fields = (
            'post',
            'author',
            'like'
        )

    def update(self, instance, validated_data):
        if 'author' in validated_data.keys():
            author = PostLike.objects.filter(id=instance.author_uuid).first()
            author_serializer = PostLikeListSerializer(author)
            author_serializer.update(author, dict(validated_data['author']))
            del validated_data['author']
        return super().update(instance, validated_data)


