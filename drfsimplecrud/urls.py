from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects.api import ProjectViewSet  # importamos tu ViewSet desde projects/api.py

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # todos los endpoints de la API van aquí
]
