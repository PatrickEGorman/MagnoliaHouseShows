from django.contrib import admin

from main.admin import meta_created_date, meta_created_by, ModelAdminWithMeta
from .models import InfoPage, Directions, History


class InfoAdmin(ModelAdminWithMeta):
    list_display = ('page_name', 'title', 'image', 'text', meta_created_date, meta_created_by)


class DirectionsAdmin(ModelAdminWithMeta):
    list_display = ('starting_point', 'title', 'image', 'text', meta_created_date, meta_created_by)


class HistoryAdmin(ModelAdminWithMeta):
    list_display = ('start_or_primary_date', 'end_date', 'title', 'image', 'text', meta_created_date,
                    meta_created_by)
    list_filter = ('start_or_primary_date', 'end_date')


admin.site.register(InfoPage, InfoAdmin)
admin.site.register(Directions, DirectionsAdmin)
admin.site.register(History, HistoryAdmin)