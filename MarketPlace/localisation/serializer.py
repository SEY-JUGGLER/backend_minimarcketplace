from rest_framework import serializers
from .models import Location, Region, Farm
from django.contrib.auth.models import User # Importe le modèle User de Django

# Sérialiseur pour le modèle User (utilisé pour afficher les détails du propriétaire de la ferme)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] # Champs à inclure dans la sérialisation de l'utilisateur

# Sérialiseur pour le modèle Location
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        # Tous les champs du modèle Location sont inclus
        fields = ['id', 'name', 'latitude', 'longitude', 'address', 'city', 'country']

# Sérialiseur pour le modèle Region
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        # Tous les champs du modèle Region sont inclus
        fields = ['id', 'name', 'description']

# Sérialiseur pour le modèle Farm
class FarmSerializer(serializers.ModelSerializer):
    # Champs en lecture seule pour afficher les détails complets des objets liés
    owner = UserSerializer(read_only=True) # Affiche les détails du propriétaire
    location = LocationSerializer(read_only=True) # Affiche les détails de la localisation
    region = RegionSerializer(read_only=True) # Affiche les détails de la région
    
    # Champs en écriture seule pour accepter les IDs des objets liés lors de la création/mise à jour
    # 'source=\'owner\'' indique que ce champ correspond à l'attribut 'owner' du modèle
    owner_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='owner', write_only=True)
    # Champ pour accepter l'ID de la localisation
    location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), source='location', write_only=True)
    # Champ pour accepter l'ID de la région (optionnel car la région peut être null)
    # 'required=False' et 'allow_null=True' permettent de créer une ferme sans région
    region_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), source='region', write_only=True, required=False, allow_null=True)

    class Meta:
        model = Farm
        # Liste de tous les champs à inclure dans la sérialisation
        # Les champs avec '_id' sont pour l'écriture, les autres pour la lecture
        fields = ['id', 'name', 'owner', 'location', 'region', 'owner_id', 'location_id', 'region_id', 'size_ha']
