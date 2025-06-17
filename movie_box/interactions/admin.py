from django.contrib import admin
from .models import watchHistory, Rating, Favorite

class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'score', 'rated_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('rated_at',)
    ordering = ('-rated_at',)

admin.site.register(Rating, RatingAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'favorited_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('favorited_at',)
    ordering = ('-favorited_at',)

admin.site.register(Favorite, FavoriteAdmin)

class watchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'watched_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('watched_at',)
    ordering = ('-watched_at',)

admin.site.register(watchHistory, watchHistoryAdmin)