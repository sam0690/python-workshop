from django.urls import path
from .views import login,signup,profile,logout
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("profile/", profile , name="profile"),
    path("logout/", logout, name="logout"),  # Assuming you have a logout view defined
]
