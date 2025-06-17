from django.shortcuts import render , redirect
from .models import Movie, Genre
from django.contrib.auth.decorators import login_required
from .forms import MovieForm
from django.views import View 
from django.views.generic import ListView, CreateView , DetailView , DeleteView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required
def index(request):
    movies = Movie.objects.all()
    trending_movie = Movie.objects.filter(is_trending=True)
    featured_movie = Movie.objects.filter(is_featured=True)
    # genres = Genre.objects.all()
    context={
        "movies": movies ,
        "user": request.user,
        "trending_movie": trending_movie,
        "featured_movie": featured_movie,
        # "genres": genres,
        }
    return render(request, "index.html" , context=context)


class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all()
        context["trending_movie"] = Movie.objects.filter(is_trending=True)
        return context



class AddMovieView(LoginRequiredMixin,CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "add_movie.html"
    success_url = "/movie_list/"
    login_url = '/login/'  # Redirect to login if not authenticated

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the currently logged-in user
        return super().form_valid(form)


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie"



class MovieUpdate(UpdateView):
    model = Movie
    template_name = "add_movie.html"
    fields = "__all__"
    success_url = "/movie_list/"
    

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = "movie_confirm_delete.html"
    success_url = "/movie_list/"
    login_url = '/login/'  # Redirect to login if not authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = self.get_object()
        return context

