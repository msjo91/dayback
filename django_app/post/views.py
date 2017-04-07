from rest_framework import generics

from post.models import Mood
from post.serializers import MoodSerializer


## 제네릭 뷰로 작성
class Mood_list(generics.ListAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer


class Mood_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
