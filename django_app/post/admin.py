from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'mood', 'photo', 'is_visible')


admin.site.register(Post, PostAdmin)
