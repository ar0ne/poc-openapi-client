"""
URL configuration for config project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .routers import urlpatterns as urlpatterns_v1


public_patterns = [
    path("api/v1/", include(urlpatterns_v1)),
]

urlpatterns = public_patterns + [
    path("openapi/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path("swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(settings.ADMIN_SITE_URL, admin.site.urls),
]
