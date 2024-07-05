from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, UniversityViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]