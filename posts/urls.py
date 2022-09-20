from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, CommentViewSet, AnaliticViewSet, PostLikeViewSet



router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('comment', CommentViewSet)
router.register('like', PostLikeViewSet)

urlpatterns = [
    # path('posts/', PostViewSet.as_view({'put': 'posts'})),
    path('delete_attachments/', PostViewSet.as_view({'delete': 'delete_attachments'})),
    path('delete_attachments/', CommentViewSet.as_view({'delete': 'delete_attachments'})),
    path('analitic/', AnaliticViewSet.as_view()),
    # re_path(r'^like_dislike/(?P<pk>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$',
    #         PostViewSet.as_view({'put': 'add_like'})),
    # path('like/', PostLikeViewSet.as_view()),

] + router.urls