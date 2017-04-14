from django.db import models

from config import settings


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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    mood_chk = models.IntegerField(choices=MOOD_CHOICE)
    mood_comment = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='post', blank=True)
    is_visible = models.BooleanField(default=True)
