from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
def index(request):

    profiles = Profile.objects.all()  # Fetch all profiles from the database

    # This function renders the index.html template with a context dictionary
    return render(request, "index.html",{"profiles": profiles})