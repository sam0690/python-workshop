from django.urls import path
from .views import index , MovieListView,AddMovieView,MovieDetailView,MovieUpdate,MovieDelete
from .api_view import get_movies,movie_detail_view

urlpatterns = [


    path("api/movies/", get_movies, name="get_movies"),  # API endpoint for movies
    path("api/movies/<int:pk>/", movie_detail_view, name="movie_detail_api"),  # API endpoint for movie detail


    path("", index, name="home"),
    path("movie_list/", MovieListView.as_view(), name="movie_list"),
    path("add_movie/",AddMovieView.as_view(), name="add_movie"),
    path("movie_detail/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie_update/<int:pk>/", MovieUpdate.as_view(), name="movie_update"),
    path("movie_delete/<int:pk>/", MovieDelete.as_view(), name="movie_delete"),
]   