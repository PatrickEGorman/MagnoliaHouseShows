from django.contrib import admin

from main.admin import meta_created_date, meta_created_by
from .models import Show


class ShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'priority', 'display_artists', 'display_genre', 'facebook', meta_created_date,
                    meta_created_by)
    list_filter = ['date', 'priority', 'genres', 'artists']
    fields = [('date', 'time'), 'artists', 'priority', 'description', ('suggested_donation', 'suggested_donation_max'),
              ('facebook', 'instagram')]


admin.site.register(Show, ShowAdmin)