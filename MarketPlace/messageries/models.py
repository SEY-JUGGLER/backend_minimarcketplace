from django.db import models

# Create your models here.

from django.conf import settings

# Modèle Message
# Représente un message envoyé entre deux utilisateurs.
class Message(models.Model):
    # Clé étrangère vers le modèle utilisateur de Django (settings.AUTH_USER_MODEL).
    # 'related_name' permet d'accéder aux messages envoyés par un utilisateur.
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    
    # Clé étrangère vers le modèle utilisateur de Django.
    # 'related_name' permet d'accéder aux messages reçus par un utilisateur.
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    
    # Contenu textuel du message.
    content = models.TextField()
    
    # Horodatage de la création du message. 'auto_now_add=True' définit la date/heure lors de la création.
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Indique si le message a été lu. Par défaut à False.
    is_read = models.BooleanField(default=False)

    # Classe Meta pour définir des options spécifiques au modèle.
    class Meta:
        # Ordonne les messages par horodatage décroissant (les plus récents en premier).
        ordering = ['-timestamp']

    # Méthode de représentation en chaîne de caractères pour une meilleure lisibilité dans l'interface d'administration.
    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.content[:50]}...'

