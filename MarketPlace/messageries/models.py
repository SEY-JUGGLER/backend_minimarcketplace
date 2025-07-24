from django.db import models

# Create your models here.

from django.conf import settings
'''
ceci est notre model de messagerie qui se chargera de gerer les differents discussion entre
le vendeur et l'acheteur , de facon personnaliser .
sender & receiver , permettre d'identier clairement qui envoie a qui.

related_name='sent_messages' permettre de recuperer tout les message envoyer par un user facilement 

related_name='received_messages' lui il fera la mm chose pour les message recu

is_read a ete implementer pour gerer la notification des messages non lue

-timestamp  permettra d'afficher les dernier message non lu en premier 
'''
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')

    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')

    # Contenu textuel du message.
    content = models.TextField()

    # Horodatage de la création du message. 'auto_now_add=True' définit la date/heure lors de la création.
    timestamp = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    # Méthode de représentation en chaîne de caractères pour une meilleure lisibilité dans l'interface d'administration.
    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.content[:50]}...'