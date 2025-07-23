from django.shortcuts import render

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Annonce, Categorie
from .serializers import AnnonceSerializer, CategorieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all().order_by('-date_pub')
    serializer_class = AnnonceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categorie', 'localisation', 'vendeur']
    search_fields = ['titre', 'description', 'localisation']
    ordering_fields = ['date_pub', 'prix']

    def perform_create(self, serializer):
        serializer.save(vendeur=self.request.user)  # vendeur connecté automatiquement

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
