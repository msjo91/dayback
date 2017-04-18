from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'url', 'author', 'created', 'mood', 'content', 'post_photo', 'is_visible')
        ordering = ('id',)
