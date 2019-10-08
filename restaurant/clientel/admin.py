from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'email',
        'numero',
        'date',
        'heure',
        'personne',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'date',
        'date_add',
        'date_update',
        'status',
        'nom',
        'email',
        'numero',
        'date',
        'heure',
        'personne',
        'date_add',
        'date_update',
        'status',
    )


class TemoignageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'commentaire',
        'image',
        'job',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'nom',
        'commentaire',
        'image',
        'job',
        'date_add',
        'date_update',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Reservation, ReservationAdmin)
_register(models.Temoignage, TemoignageAdmin)
