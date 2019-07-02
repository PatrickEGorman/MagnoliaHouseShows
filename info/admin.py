from django.contrib import admin
from .models import InfoPage, Directions


class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text')


class DirectoinsAdmin(admin.ModelAdmin):
    list_display = ('starting_point', 'title', 'image', 'text')



admin.site.register(InfoPage)
admin.site.register(Directions)