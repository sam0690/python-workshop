from django.contrib import admin
from .models import Recommendation

# Register your models here.
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'score', 'created_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Recommendation, RecommendationAdmin)