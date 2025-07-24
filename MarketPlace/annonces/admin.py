from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Annonce, Categorie

admin.site.register(Annonce)
admin.site.register(Categorie)