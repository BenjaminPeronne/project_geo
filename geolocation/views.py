from rest_framework import viewsets
from .models import Etudiant, Universite
from .serializers import EtudiantSerializer, UniversiteSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UniversiteViewSet(viewsets.ModelViewSet):
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def map_view(request):
    return render(request, 'geolocation/map.html')