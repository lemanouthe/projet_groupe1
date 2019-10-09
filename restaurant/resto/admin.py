from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_update', 'status')
    list_filter = (
        'date_add',
        'status',
    )


class IngredientAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_update', 'status')
    list_filter = (
        'date_add',
        'status',
    )


class PlatAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'nom',
        'prix',
        'image',
        'speciale',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'categorie',
        'speciale',
        'date_add',
        'status',
    )
    raw_id_fields = ('ingredient',)


class PosteAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_update', 'status')
    list_filter = (
        'date_add',

        'status',
    )


class personnelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'prenom',
        'photo',
        'poste',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'poste',
        'date_add',
        
        'status',
    )
    raw_id_fields = ('social',)


class PlaceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nb_place_disponible',
        'nb_place_total',
        'date_add',
        'date_update',
    )
    list_filter = (
        'date_add',
        'date_update',
        'nb_place_disponible',
        'nb_place_total',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Ingredient, IngredientAdmin)
_register(models.Plat, PlatAdmin)
_register(models.Poste, PosteAdmin)
_register(models.Personnel, personnelAdmin)
_register(models.Place, PlaceAdmin)
