from django.contrib import admin
from .models import Show


class ShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'display_artists', 'facebook', 'display_genre')
    list_filter = ['date', 'genres', 'artists']
    fields = [('date', 'time'), 'artists', 'description', ('suggested_donation', 'suggested_donation_max'),
              ('facebook', 'instagram')]


admin.site.register(Show, ShowAdmin)