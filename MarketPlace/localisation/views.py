from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Location, Region, Farm
from .serializer import LocationSerializer, RegionSerializer, FarmSerializer

# ViewSet pour le modèle Location
# Fournit les opérations CRUD standard pour les localisations
class LocationViewSet(viewsets.ModelViewSet):
    # Définit l'ensemble des objets Location que ce ViewSet va gérer
    queryset = Location.objects.all()
    # Spécifie le sérialiseur à utiliser pour les objets Location
    serializer_class = LocationSerializer

# ViewSet pour le modèle Region
class RegionViewSet(viewsets.ModelViewSet):
    # Définit l'ensemble des objets Region que ce ViewSet va gérer
    queryset = Region.objects.all()
    # Spécifie le sérialiseur à utiliser pour les objets Region
    serializer_class = RegionSerializer

    # Action personnalisée pour récupérer toutes les fermes d'une région spécifique
    # @action(detail=True) signifie que cette action nécessite un ID de région
    # URL: /api/localisation/regions/{id}/farms/
    @action(detail=True, methods=['get'])
    def farms(self, request, pk=None):
        """
        Endpoint personnalisé pour récupérer toutes les fermes d'une région donnée.
        URL: /api/localisation/regions/{id}/farms/
        """
        # Récupère l'objet Region correspondant à l'ID fourni
        region = self.get_object()
        
        # Filtre toutes les fermes qui appartiennent à cette région
        farms = Farm.objects.filter(region=region)
        
        # Sérialise la liste des fermes en utilisant le FarmSerializer
        serializer = FarmSerializer(farms, many=True)
        return Response(serializer.data)

# ViewSet pour le modèle Farm
class FarmViewSet(viewsets.ModelViewSet):
    # Définit l'ensemble des objets Farm que ce ViewSet va gérer
    queryset = Farm.objects.all()
    # Spécifie le sérialiseur à utiliser pour les objets Farm
    serializer_class = FarmSerializer

    # Action personnalisée pour récupérer les fermes de l'utilisateur connecté
    # @action(detail=False) car cette action ne nécessite pas d'ID spécifique
    # URL: /api/localisation/farms/my_farms/
    @action(detail=False, methods=['get'])
    def my_farms(self, request):
        """
        Endpoint personnalisé pour récupérer toutes les fermes appartenant à l'utilisateur connecté.
        URL: /api/localisation/farms/my_farms/
        """
        # Vérifie si l'utilisateur est authentifié
        if request.user.is_authenticated:
            # Filtre les fermes où le propriétaire est l'utilisateur connecté
            farms = Farm.objects.filter(owner=request.user)
            # Sérialise la liste des fermes
            serializer = self.get_serializer(farms, many=True)
            return Response(serializer.data)
        # Si l'utilisateur n'est pas authentifié, retourne une erreur 401
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    # Action personnalisée pour filtrer les fermes par région
    # Cette action utilise un paramètre de requête (query parameter) au lieu d'un paramètre d'URL
    # URL: /api/localisation/farms/by_region/?region_id=1
    @action(detail=False, methods=['get'])
    def by_region(self, request):
        """
        Endpoint personnalisé pour filtrer les fermes par région.
        Utilise un paramètre de requête 'region_id'.
        URL: /api/localisation/farms/by_region/?region_id={region_id}
        """
        # Récupère le paramètre 'region_id' de la requête GET
        # request.query_params est un dictionnaire contenant tous les paramètres de requête
        region_id = request.query_params.get('region_id')
        
        # Vérifie si le paramètre region_id a été fourni
        if region_id:
            # Filtre les fermes par l'ID de région fourni
            farms = Farm.objects.filter(region_id=region_id)
            # Sérialise la liste des fermes filtrées
            serializer = self.get_serializer(farms, many=True)
            return Response(serializer.data)
        
        # Si le paramètre region_id n'est pas fourni, retourne une erreur 400 (Bad Request)
        return Response({'error': 'region_id parameter required'}, status=status.HTTP_400_BAD_REQUEST)
