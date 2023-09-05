from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MoviesData

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(types='action')
    serializer_class = MovieSerializer


class DramaViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(types='drama')
    serializer_class = MovieSerializer


class ComdeyViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(types='comdey')
    serializer_class = MovieSerializer