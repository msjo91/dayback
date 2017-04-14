import django_filters
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .models import Post
from .serializers import PostSerializer

User = get_user_model()


class PostFilter(django_filters.rest_framework.FilterSet):
    year = django_filters.NumberFilter(name='created_date', lookup_expr='year')
    month = django_filters.NumberFilter(name='created_date', lookup_expr='month')
    day = django_filters.NumberFilter(name='created_date', lookup_expr='day')

    class Meta:
        model = Post
        fields = ('year', 'month', 'day',)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_class = PostFilter
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
