"""
Django settings for drfsimplecrud project.
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-7nt8#brsk2_k8ex424_b!&64nz1jfcc9kasc^wc+4^ep-0ndtj")

# DEBUG: usar True en local, False en Render/producción
DEBUG = os.getenv("DEBUG", "True") == "True"

# Hosts permitidos
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "django2-xo79.onrender.com",
]

# Si usas frontend en otro dominio, configúralo aquí
CSRF_TRUSTED_ORIGINS = [
    "https://django2-xo79.onrender.com",
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # DRF
    "rest_framework",

    # CORS
    "corsheaders",

    # Tus apps
    "projects",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Whitenoise para archivos estáticos en producción
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    # CORS
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "drfsimplecrud.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # aquí puedes agregar templates propios
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "drfsimplecrud.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"

# Carpeta donde se recopilan los archivos estáticos para producción
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Archivos estáticos adicionales (opcional)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "projects", "static"),  # si tienes CSS/JS propio
]

# Whitenoise compresión en producción
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configuración de Django Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",  # siempre JSON
        "rest_framework.renderers.BrowsableAPIRenderer",  # interfaz web
    ]
}

# CORS configuración
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ solo para pruebas, en prod usa lista segura
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
#     "https://tu-frontend.com",
# ]
