"""
General router config
"""

from rest_framework.routers import DefaultRouter

from books.views import BookViewSet


router = DefaultRouter()

router.register(r"books", BookViewSet, "books")


urlpatterns = router.urls
