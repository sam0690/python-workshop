from django.shortcuts import render
from .models import Rating, Favorite, watchHistory
from django.views.generic import ListView , CreateView, DetailView, DeleteView, UpdateView
# Create your views here.

class ratingListView(ListView):
    model = Rating
    template_name = "index.html"
    context_object_name = "ratings"

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)
    
class FavoriteListView(ListView):
    model = Favorite
    template_name = "favorites.html"
    context_object_name = "favorites"

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    

class WatchHistoryListView(ListView):
    model = watchHistory
    template_name = "watch_history.html"
    context_object_name = "watch_histories"

    def get_queryset(self):
        return watchHistory.objects.filter(user=self.request.user)