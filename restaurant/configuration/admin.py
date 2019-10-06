from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class DayAdmin(admin.ModelAdmin):

    list_display = ('id', 'jour', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'jour',
        'status',
        'date_add',
        'date_upd',
    )


class WorkingHourAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'jour',
        'start_hour',
        'end_hour',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'jour',
        'status',
        'date_add',
        'date_upd',
        'id',
        'jour',
        'start_hour',
        'end_hour',
        'status',
        'date_add',
        'date_upd',
    )


class PresentationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'description',
        'image',
        'text_accueil',
        'lien_video',
        'text1',
        'text2',
        'text3',
        'license_site',
        'status',
        'date_add',
        'date_udp',
    )
    list_filter = (
        'status',
        'date_add',
        'date_udp',
        'id',
        'nom',
        'description',
        'image',
        'text_accueil',
        'lien_video',
        'text1',
        'text2',
        'text3',
        'license_site',
        'status',
        'date_add',
        'date_udp',
    )
    raw_id_fields = ('working_hour',)


class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_udp',
    )
    list_filter = (
        'status',
        'date_add',
        'date_udp',
        'id',
        'nom',
        'description',
        'image',
        'status',
        'date_add',
        'date_udp',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'lien',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class ReserveConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'sous_titre',
        'image',
        'status',
        'date_add',
        'date_udp',
    )
    list_filter = (
        'status',
        'date_add',
        'date_udp',
        'id',
        'titre',
        'sous_titre',
        'image',
        'status',
        'date_add',
        'date_udp',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Day, DayAdmin)
_register(models.WorkingHour, WorkingHourAdmin)
_register(models.Presentation, PresentationAdmin)
_register(models.About, AboutAdmin)
_register(models.Social, SocialAdmin)
_register(models.ReserveConfig, ReserveConfigAdmin)
