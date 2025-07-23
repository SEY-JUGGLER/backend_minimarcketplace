from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User # Importe le modèle User de Django

# Sérialiseur pour le modèle User (utilisé pour afficher les détails de l'expéditeur/destinataire)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] # Champs à inclure dans la sérialisation de l'utilisateur

# Sérialiseur pour le modèle Message
class MessageSerializer(serializers.ModelSerializer):
    # Champ en lecture seule pour afficher les détails complets de l'expéditeur
    sender = UserSerializer(read_only=True)
    # Champ en lecture seule pour afficher les détails complets du destinataire
    receiver = UserSerializer(read_only=True)
    
    # Champ en écriture seule pour accepter l'ID de l'expéditeur lors de la création/mise à jour
    # 'source=\'sender\'' indique que ce champ correspond à l'attribut 'sender' du modèle
    # 'write_only=True' signifie que ce champ est utilisé uniquement pour l'entrée (POST/PUT/PATCH)
    sender_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='sender', write_only=True)
    # Champ en écriture seule pour accepter l'ID du destinataire
    receiver_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='receiver', write_only=True)

    class Meta:
        model = Message
        # Liste de tous les champs à inclure dans la sérialisation.
        # 'sender' et 'receiver' sont pour la lecture, 'sender_id' et 'receiver_id' pour l'écriture.
        fields = ['id', 'sender', 'receiver', 'sender_id', 'receiver_id', 'content', 'timestamp', 'is_read']
        # Champs qui ne peuvent être que lus (non modifiables via l'API lors de la création/mise à jour)
        read_only_fields = ['timestamp'] # Le timestamp est généré automatiquement par le modèle

