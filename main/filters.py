from django_filters.rest_framework import FilterSet

from .models import Genres, MusicModel


class MusicFilter(FilterSet):
    class Meta:
        model = MusicModel
        fields = {
            'title': ['exact'],
        }
    