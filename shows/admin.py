from django.contrib import admin
from .models import Show


class ShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'bands')


admin.site.register(Show, ShowAdmin)