from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message
from .serializer import MessageSerializer

# ViewSet pour le modèle Message
# ModelViewSet fournit automatiquement les actions CRUD (Create, Retrieve, Update, Delete)
class MessageViewSet(viewsets.ModelViewSet):
    # Définit l'ensemble des objets que ce ViewSet va gérer
    # Ici, tous les messages de la base de données
    queryset = Message.objects.all()
    
    # Spécifie le sérialiseur à utiliser pour convertir les objets Message en JSON et vice versa
    serializer_class = MessageSerializer

    # Action personnalisée pour récupérer les messages envoyés par l'utilisateur connecté
    # @action(detail=False) signifie que cette action ne nécessite pas d'ID spécifique (pas de /messages/{id}/sent_messages/)
    # mais plutôt /messages/sent_messages/
    # methods=['get'] indique que cette action répond uniquement aux requêtes GET
    @action(detail=False, methods=['get'])
    def sent_messages(self, request):
        """
        Endpoint personnalisé pour récupérer tous les messages envoyés par l'utilisateur connecté.
        URL: /api/messageries/messages/sent_messages/
        """
        # Vérifie si l'utilisateur est authentifié
        if request.user.is_authenticated:
            # Filtre les messages où l'expéditeur est l'utilisateur connecté
            messages = Message.objects.filter(sender=request.user)
            # Sérialise la liste des messages (many=True pour une liste d'objets)
            serializer = self.get_serializer(messages, many=True)
            # Retourne la réponse avec les données sérialisées
            return Response(serializer.data)
        # Si l'utilisateur n'est pas authentifié, retourne une erreur 401
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    # Action personnalisée pour récupérer les messages reçus par l'utilisateur connecté
    @action(detail=False, methods=['get'])
    def received_messages(self, request):
        """
        Endpoint personnalisé pour récupérer tous les messages reçus par l'utilisateur connecté.
        URL: /api/messageries/messages/received_messages/
        """
        if request.user.is_authenticated:
            # Filtre les messages où le destinataire est l'utilisateur connecté
            messages = Message.objects.filter(receiver=request.user)
            serializer = self.get_serializer(messages, many=True)
            return Response(serializer.data)
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    # Action personnalisée pour marquer un message spécifique comme lu
    # @action(detail=True) signifie que cette action nécessite un ID spécifique
    # URL: /api/messageries/messages/{id}/mark_as_read/
    # methods=['patch'] indique que cette action répond aux requêtes PATCH (mise à jour partielle)
    @action(detail=True, methods=['patch'])
    def mark_as_read(self, request, pk=None):
        """
        Endpoint personnalisé pour marquer un message comme lu.
        URL: /api/messageries/messages/{id}/mark_as_read/
        """
        # Récupère l'objet Message correspondant à l'ID fourni (pk)
        # get_object() est une méthode du ViewSet qui gère automatiquement les erreurs 404
        message = self.get_object()
        
        # Modifie le statut du message pour le marquer comme lu
        message.is_read = True
        # Sauvegarde les modifications en base de données
        message.save()
        
        # Sérialise le message mis à jour et le retourne
        serializer = self.get_serializer(message)
        return Response(serializer.data)
