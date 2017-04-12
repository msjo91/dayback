import django_filters
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .models import Post
from .serializers import PostSerializer

User = get_user_model()


class PostFilter(django_filters.rest_framework.FilterSet):
    created_date_year = django_filters.NumberFilter(name='created_date', lookup_expr='year')
    created_date_month = django_filters.NumberFilter(name='created_date', lookup_expr='month')
    created_date_day = django_filters.NumberFilter(name='created_date', lookup_expr='day')

    class Meta:
        model = Post
        fields = ('created_date_year', 'created_date_month', 'created_date_day')


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_class = PostFilter
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    # def perform_create(self, validated_data):
    #     post = Post.objects.create_post(
    #         author=User.objects.get(self.request.user),
    #         mood_chk=validated_data['mood_chk'],
    #         mood_comment=validated_data['mood_comment']
    #     )
    #     post.save()
    #     return post
