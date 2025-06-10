from django.shortcuts import render
from .models import Post
from .models import Members , Viewers

def index(request):
     
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "post_detail.html",context={"post": post})

def members(request):
    members = Members.objects.all()
    return render(request, "members.html", {"members": members})

def Viewers(request):
    viewers = Viewers.objects.all()
    return render(request, "viewers.html", {"viewers": viewers})