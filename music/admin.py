from django.contrib import admin
from .models import Album, Band, Genre, Song


admin.site.register(Album)
admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Song)