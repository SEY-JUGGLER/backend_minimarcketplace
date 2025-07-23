from django.db import models

# Create your models here.
from django.conf import settings

# Modèle Location
# Représente une localisation géographique avec des coordonnées GPS.
class Location(models.Model):
    # Nom de la localisation.
    name = models.CharField(max_length=255)
    
    # Latitude en degrés décimaux. 'max_digits=9' et 'decimal_places=6' permettent une précision GPS élevée.
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    # Longitude en degrés décimaux.
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    # Adresse complète (optionnelle).
    address = models.CharField(max_length=255, blank=True, null=True)
    
    # Ville (optionnelle).
    city = models.CharField(max_length=100, blank=True, null=True)
    
    # Pays (optionnel).
    country = models.CharField(max_length=100, blank=True, null=True)

    # Méthode de représentation en chaîne de caractères.
    def __str__(self):
        return self.name

# Modèle Region
# Représente une région administrative ou géographique.
class Region(models.Model):
    # Nom unique de la région.
    name = models.CharField(max_length=255, unique=True)
    
    # Description optionnelle de la région.
    description = models.TextField(blank=True, null=True)

    # Méthode de représentation en chaîne de caractères.
    def __str__(self):
        return self.name

# Modèle Farm
# Représente une exploitation agricole avec sa localisation et son propriétaire.
class Farm(models.Model):
    # Nom de l'exploitation agricole.
    name = models.CharField(max_length=255)
    
    # Propriétaire de l'exploitation (clé étrangère vers le modèle utilisateur).
    # 'related_name' permet d'accéder aux exploitations d'un utilisateur.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farms')
    
    # Localisation de l'exploitation (relation un-à-un avec Location).
    # 'OneToOneField' garantit qu'une localisation ne peut être associée qu'à une seule exploitation.
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    
    # Région à laquelle appartient l'exploitation (optionnelle).
    # 'SET_NULL' permet de conserver l'exploitation même si la région est supprimée.
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Superficie de l'exploitation en hectares (optionnelle).
    # 'max_digits=10' et 'decimal_places=2' permettent des valeurs jusqu'à 99,999,999.99 ha.
    size_ha = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Méthode de représentation en chaîne de caractères.
    def __str__(self):
        return self.name