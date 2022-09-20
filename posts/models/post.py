from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker
from utils.const import PostKindChoice



class Post(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(
        max_length=500,
        verbose_name='Title'
    )
    text = models.CharField(
        max_length=100,
        verbose_name='Text'
    )
    kind = models.CharField(
        max_length=100,
        choices=PostKindChoice.choice(),
        default=PostKindChoice.BLOG.value,
    )
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('uuid', )


