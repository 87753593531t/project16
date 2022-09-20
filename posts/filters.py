# import django_filters
# from django.db.models import Q
from django_filters import rest_framework as filters

from posts.models import PostLike

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass



class PostLikeFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='updated_at', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='updated_at', lookup_expr='lte')

    class Meta:
        model = PostLike
        fields = ('date_from', 'date_to')
    # post = CharFilterInFilter(field_name='updated_at', lookup_expr='in')
    # # updated_at = filters.RangeFilter()
    #
    # class Meta:
    #     model = Post
    #     fields = ['post', 'updated_at']