from django.db import models
from django.core.exceptions import ValidationError
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError
import ssl

ssl_context = ssl._create_unverified_context()

class Universite(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20)
    pays = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            try:
                geolocator = Nominatim(user_agent="geolocation", ssl_context=ssl_context)
                location = geolocator.geocode(f"{self.adresse}, {self.ville}, {self.code_postal}, {self.pays}")
                if location:
                    self.latitude = location.latitude
                    self.longitude = location.longitude
            except GeocoderServiceError as e:
                print(f"Geocoding error: {e}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20)
    pays = models.CharField(max_length=100)
    universite = models.ForeignKey(Universite, on_delete=models.SET_NULL, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            try:
                geolocator = Nominatim(user_agent="geolocation", ssl_context=ssl_context)
                location = geolocator.geocode(f"{self.adresse}, {self.ville}, {self.code_postal}, {self.pays}")
                if location:
                    self.latitude = location.latitude
                    self.longitude = location.longitude
            except GeocoderServiceError as e:
                print(f"Geocoding error: {e}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prenom} {self.nom}"