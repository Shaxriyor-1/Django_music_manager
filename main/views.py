# from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from main.filters import MusicFilter

from .models import Genres, MusicModel
from .serializers import genres_serializer, music_serializer


# Create your views here.
class music_viewset(viewsets.ModelViewSet):
    queryset=MusicModel.objects.all()
    serializer_class=music_serializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MusicFilter
    filter_fields = '__all__'
    search_fields = ['title', 'genre']
    ordering_fields = ['title']
    
class genre_viewset(viewsets.ModelViewSet):
    queryset=Genres.objects.all()
    serializer_class=genres_serializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['genre']
    search_fields = '__all__'
    

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = music_serializer
    queryset = MusicModel.objects.all()

class GenresDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = genres_serializer
    queryset = Genres.objects.all()
