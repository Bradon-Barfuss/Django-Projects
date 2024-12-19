from django.shortcuts import render
from rest_framework import viewsets
from .models import BookData
from .serializers import BookSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class NonFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='non-fiction')
    serializer_class = BookSerializer

class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fiction')
    serializer_class = BookSerializer

class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='mystery')
    serializer_class = BookSerializer

class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='science-fiction')
    serializer_class = BookSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='romance')
    serializer_class = BookSerializer

class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='thriller')
    serializer_class = BookSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='biography')
    serializer_class = BookSerializer

class SelfHelpViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='self-help')
    serializer_class = BookSerializer

class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='historical-fiction')
    serializer_class = BookSerializer

