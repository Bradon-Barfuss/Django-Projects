
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from books.views import BookViewSet, NonFictionViewSet, FictionViewSet, MysteryViewSet, ScienceFictionViewSet, RomanceViewSet, ThrillerViewSet, FantasyViewSet, BiographyViewSet, SelfHelpViewSet, HistoricalFictionViewSet
from rest_framework.routers import SimpleRouter
router = SimpleRouter()

router.register(r'books', BookViewSet, basename='books')
router.register(r'non-fiction', NonFictionViewSet, basename='non-fiction')
router.register(r'fiction', FictionViewSet, basename='fiction')
router.register(r'mystery', MysteryViewSet, basename='mystery')
router.register(r'science-fiction', ScienceFictionViewSet, basename='science-fiction')
router.register(r'romance', RomanceViewSet, basename='romance')
router.register(r'thriller', ThrillerViewSet, basename='thriller')
router.register(r'fantasy', FantasyViewSet, basename='fantasy')
router.register(r'biography', BiographyViewSet, basename='biography')
router.register(r'self-help', SelfHelpViewSet, basename='self-help')
router.register(r'historical-fiction', HistoricalFictionViewSet, basename='historical-fiction')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
