from django.contrib import admin
from .models import Universite, Etudiant  # Mettez à jour les noms des modèles

admin.site.register(Universite)
admin.site.register(Etudiant)