from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.api import ProjectViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include(router.urls)),      # Projects en /api/projects/
    path("api/blog/", include("blog.urls")),          # Blog en /api/blog/
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
