from django.urls import path
from .views import FavoriteListView

urlpatterns = [
    path("favorites/", FavoriteListView.as_view(), name="favorites"),
]
