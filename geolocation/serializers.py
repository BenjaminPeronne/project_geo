from rest_framework import serializers
from .models import Etudiant, Universite

class UniversiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universite
        fields = '__all__'

class EtudiantSerializer(serializers.ModelSerializer):
    universite = UniversiteSerializer(read_only=True)

    class Meta:
        model = Etudiant
        fields = '__all__'