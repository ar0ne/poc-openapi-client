"""
General router config
"""

from rest_framework.routers import DefaultRouter

from books.views import BooksViewSet


router = DefaultRouter()

router.register(r"books", BooksViewSet, "books")


urlpatterns = router.urls
