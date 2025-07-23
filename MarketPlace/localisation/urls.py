
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, RegionViewSet, FarmViewSet

# Crée un routeur par défaut pour enregistrer les ViewSets de l'application localisation.
router = DefaultRouter()

# Enregistre le LocationViewSet avec le préfixe 'locations'.
# Cela créera des URLs comme /locations/, /locations/{id}/, etc.
router.register(r'locations', LocationViewSet)

# Enregistre le RegionViewSet avec le préfixe 'regions'.
# Cela créera des URLs comme /regions/, /regions/{id}/, /regions/{id}/farms/, etc.
router.register(r'regions', RegionViewSet)

# Enregistre le FarmViewSet avec le préfixe 'farms'.
# Cela créera des URLs comme /farms/, /farms/{id}/, /farms/my_farms/, /farms/by_region/, etc.
router.register(r'farms', FarmViewSet)

# Définit les motifs d'URL pour l'application localisation.
urlpatterns = [
    # Inclut toutes les URLs générées par le routeur.
    # Le chemin vide signifie que ces URLs seront accessibles directement sous le préfixe défini dans le urls.py principal.
    path('', include(router.urls)),
]
