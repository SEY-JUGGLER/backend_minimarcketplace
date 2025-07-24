from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnonceViewSet, CategorieViewSet

router = DefaultRouter()
router.register(r'annonces', AnnonceViewSet, basename='annonce')
router.register(r'categories', CategorieViewSet, basename='categorie')

urlpatterns = [
    path('', include(router.urls)),
]