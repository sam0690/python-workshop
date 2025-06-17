from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.contrib.auth.views import LoginView, LogoutView


from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Try authenticating with username first
        user = authenticate(request, username=username_or_email, password=password)

        # If not found, try authenticating with email
        if user is None:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Replace 'home' with your home page URL name
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')



def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error": "Email already exists"})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, "signup.html", {"message": f"Signed up as {username}"})
    return render(request, "signup.html")




def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"user": request.user})
    else:
        messages.error(request, "You need to be logged in to view your profile")
        return redirect("login")
    
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, "You have been logged out successfully.")
    else:
        messages.error(request, "You are not logged in.")
    return redirect("login")  # Redirect to the login page or home page after logout