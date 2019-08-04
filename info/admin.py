from django.contrib import admin

from main.admin import meta_created_date, meta_created_by, ModelAdminWithMeta
from .models import InfoPage, History


class InfoAdmin(ModelAdminWithMeta):
    list_display = ('page_name', 'title', 'text', meta_created_date, meta_created_by)
    fields = ('page_name', 'title', 'text', 'priority')


class HistoryAdmin(ModelAdminWithMeta):
    list_display = ('start_or_primary_date', 'end_date', 'title', meta_created_date,
                    meta_created_by)
    list_filter = ('start_or_primary_date', 'end_date')
    fields = ('title',  ('start_or_primary_date', 'end_date', 'approximate_date'), ('shows', 'artists'),
              ('photo', 'flier', 'youtube_video'), 'text', 'priority')


admin.site.register(InfoPage, InfoAdmin)
admin.site.register(History, HistoryAdmin)