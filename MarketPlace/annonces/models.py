from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # on suppose que le collègue 1 a défini un modèle User personnalisé

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Annonce(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='annonces/', null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    localisation = models.CharField(max_length=100)
    date_pub = models.DateTimeField(auto_now_add=True)
    vendeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="annonces")

    def __str__(self):
        return self.titre