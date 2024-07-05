from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EtudiantViewSet, UniversiteViewSet, map_view

router = DefaultRouter()
router.register(r'etudiants', EtudiantViewSet)
router.register(r'universites', UniversiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('map/', map_view, name='map'),
]