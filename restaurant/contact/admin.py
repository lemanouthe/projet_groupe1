from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'sujet',
        'email',
        'message',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'sujet',
        'email',
        'message',
        'status',
        'date_add',
        'date_upd',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'email',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Message, MessageAdmin)
_register(models.Newsletter, NewsletterAdmin)
