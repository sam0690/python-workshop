from django.contrib import admin
from .models import Movie, Genre

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'duration', 'language')
    search_fields = ('title', 'description')
    list_filter = ('language', 'release_year')
    ordering = ('-release_year',)

admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(Genre)

