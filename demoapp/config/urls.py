"""
URL configuration for config project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .routers import urlpatterns as urlpatterns_v1


schema_view = get_schema_view(
   openapi.Info(
      title="Demo API",
      default_version='v1',
      description="Demo API description",
      terms_of_service="https://example.com",
      contact=openapi.Contact(email="contact@example.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

public_patterns = [
    path("api/v1/", include(urlpatterns_v1)),
]

urlpatterns = public_patterns + [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(r"^$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_SITE_URL, admin.site.urls),
]
