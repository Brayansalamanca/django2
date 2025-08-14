from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.api import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
