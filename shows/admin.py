from django.contrib import admin

from main.admin import meta_created_date, meta_created_by, ModelAdminWithMeta, meta_updated_by, meta_updated_date
from .models import Show


class ShowAdmin(ModelAdminWithMeta):
    list_display = ('date', 'cancelled', 'priority', 'display_artists', 'display_genre', 'facebook', meta_created_date,
                    meta_created_by, meta_updated_by, meta_updated_date)
    list_filter = ['date', 'priority', 'artists', 'cancelled']
    fields = [('date', 'time'), 'artists', 'priority', 'description', ('suggested_donation', 'suggested_donation_max'),
              ('facebook', 'instagram'), 'cancelled']
    ordering = ['-date']


admin.site.register(Show, ShowAdmin)
