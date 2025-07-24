"""
urls.py - Configuration des routes pour l'application de messagerie

Ce fichier configure les URLs liées à la messagerie entre utilisateurs (vendeur et acheteur).
Il utilise un routeur DRF (`DefaultRouter`) pour générer automatiquement les endpoints REST
du `MessageViewSet`, qui fournit les opérations CRUD (Create, Read, Update, Delete) ainsi
que des actions personnalisées pour les messages envoyés, reçus et marqués comme lus.

Endpoints générés automatiquement :
- /messages/ : liste et création de messages
- /messages/{id}/ : consultation, mise à jour ou suppression d’un message
- /messages/sent_messages/ : messages envoyés par l’utilisateur connecté
- /messages/received_messages/ : messages reçus par l’utilisateur connecté
- /messages/{id}/mark_as_read/ : marquer un message comme lu
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
