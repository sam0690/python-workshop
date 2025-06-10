
from django.urls import path
from .views import index , post_detail , members

urlpatterns = [
    path("",index,name="home"),
    path("<int:pk>/",post_detail, name='post_detail'),
    path("members/", members, name='members'),
]
