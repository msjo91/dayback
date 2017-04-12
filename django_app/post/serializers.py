from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created_date', 'mood_chk', 'mood_comment')
        ordering = ('created_date',)
