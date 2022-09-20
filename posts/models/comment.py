from django.db import models
#
#
from utils.models import AbstractUUID, AbstractTimeTracker


class Comment(AbstractUUID, AbstractTimeTracker):

    comment = models.CharField(
        max_length=100,
        verbose_name='comment',
        null=True,
        blank=True
    )
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments'
    )



    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('uuid',)
