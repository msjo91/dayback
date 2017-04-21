from django.contrib.auth import get_user_model
from django.db import models

from config import settings

User = get_user_model()


class Post(models.Model):
    MOOD_VERY_BAD = 1
    MOOD_BAD = 2
    MOOD_GOOD = 3
    MOOD_VERY_GOOD = 4

    MOOD_CHOICE = (
        (MOOD_VERY_GOOD, 'VeryGood'),
        (MOOD_GOOD, 'Good'),
        (MOOD_BAD, 'Bad'),
        (MOOD_VERY_BAD, 'VeryBad'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    mood = models.IntegerField(choices=MOOD_CHOICE)
    content = models.TextField(max_length=400, blank=True, null=True)
    post_photo = models.ImageField(upload_to='post', blank=True, null=True)
    is_visible = models.BooleanField(default=True)
