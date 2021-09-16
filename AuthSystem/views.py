from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('home/')

    context = {
        'login_form': form,
    }
    return render(request, "login.html", context)

def homeview(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect('login/')