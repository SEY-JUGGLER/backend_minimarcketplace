

from rest_framework import serializers
from .models import Message
from django.contrib.auth import get_user_model
User = get_user_model()

"""
Sérialiseur pour le modèle Message.

Ce sérialiseur permet à la fois :
- d'afficher les détails complets de l'expéditeur et du destinataire via des champs de lecture seule,
- d'accepter leurs identifiants (IDs) lors de la création ou la mise à jour d'un message via des champs d'écriture seule.

Champs exposés :
- sender (lecture seule)      : Détails de l'utilisateur ayant envoyé le message.
- receiver (lecture seule)    : Détails de l'utilisateur ayant reçu le message.
- sender_id (écriture seule)  : ID de l'utilisateur expéditeur.
- receiver_id (écriture seule): ID de l'utilisateur destinataire.
- content                     : Contenu du message.
- timestamp (lecture seule)   : Date et heure de l'envoi du message.
- is_read                     : Indique si le message a été lu.
"""



# Sérialiseur pour le modèle User (utilisé pour afficher les détails de l'expéditeur/destinataire)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Champs à inclure dans la sérialisation de l'utilisateur


# Sérialiseur pour le modèle Message
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='sender', write_only=True)
    receiver_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='receiver', write_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'sender_id', 'receiver_id', 'content', 'timestamp', 'is_read']
        read_only_fields = ['timestamp']  # Le timestamp est généré automatiquement par le modèle