from rest_framework import serializers

from .models import Genres, MusicModel


class music_serializer(serializers.ModelSerializer):
    class Meta:
        model=MusicModel
        fields='__all__'

class genres_serializer(serializers.ModelSerializer):
    class Meta:
        model=Genres
        fields='__all__'
