from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





# Create your views here.

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user.is_admin:
            print(user.user_type)
            login(request, user)
            return redirect('/')
        elif user.user_type == "Student":
            login(request, user)
            return redirect('studenthome/')
        elif user.user_type == "Teacher":
            login(request, user)
            return redirect('teacherhome/')
        elif user.user_type == "Parent":
            login(request, user)
            return redirect('parenthome/')

    context = {
        'login_form': form,
    }
    return render(request, "login.html", context)

@login_required(login_url='login')
def indexView(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def studentHomeView(request):
    context = {}
    student_obj = UserProfile.objects.filter(email = request.user.email)
    context = {
        'students' : student_obj,
    }
    return render(request, "studenthome.html", context)

@login_required(login_url='login')
def teacherHomeView(request):
    context = {}
    teacher_obj = UserProfile.objects.filter(email = request.user.email)
    context = {
        'teachers' : teacher_obj,
    }
    return render(request, "teacherhome.html", context)

@login_required(login_url='login')
def parentHomeView(request):
    context = {}
    parent_obj = UserProfile.objects.filter(email = request.user.email)
    context = {
        'parents' : parent_obj,
    }
    return render(request, "parenthome.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

def dashboard_view():
    return redirect('admin/')