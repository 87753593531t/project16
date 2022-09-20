from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker
from utils.const import UserLikeChoice
from users.models import CustomUser



class PostLike(AbstractUUID, AbstractTimeTracker):

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name="like",
        blank=True,
        null=True
    )
    like = models.CharField(max_length=100,
                            choices=UserLikeChoice.choice(),
                            default=UserLikeChoice.OK.value, )


    class Meta:
        verbose_name ='PostLike'
        verbose_name_plural = 'PostLikes'

        ordering = ('uuid', )