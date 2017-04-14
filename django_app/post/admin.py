from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'is_visible')


admin.site.register(Post, PostAdmin)
