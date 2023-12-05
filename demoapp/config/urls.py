"""
URL configuration for config project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .routers import urlpatterns as urlpatterns_v1


public_patterns = [
    path("api/v1/", include(urlpatterns_v1)),
]

urlpatterns = public_patterns + [
    path(settings.ADMIN_SITE_URL, admin.site.urls),

]
