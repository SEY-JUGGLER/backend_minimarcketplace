from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

# Crée un routeur par défaut pour enregistrer les ViewSets.
# Le routeur génère automatiquement les schémas d'URL pour les opérations CRUD.
router = DefaultRouter()
# Enregistre le MessageViewSet avec le préfixe 'messages'.
# Cela créera des URLs comme /messages/, /messages/{id}/, etc.
router.register(r'messages', MessageViewSet)

# Définit les motifs d'URL pour l'application messageries.
urlpatterns = [
    # Inclut toutes les URLs générées par le routeur.
    # Le chemin vide signifie que ces URLs seront accessibles directement sous le préfixe défini dans le urls.py principal.
    path('', include(router.urls)),
]
