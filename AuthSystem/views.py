from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserLoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import uuid
from django.conf import settings  
from django.core.mail import send_mail 
from django.contrib import messages

# Create your views here.
def register_view(request):
    context = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                email = request.POST.get('email')
                username = request.POST.get('username')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                phone = request.POST.get('phone')
                password = request.POST.get('password1')
                city = request.POST.get('city')
                state = request.POST.get('state')
                country = request.POST.get('country')
                auth_token = str(uuid.uuid4())
                user_obj = UserProfile.objects.create(
                    email=email,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    city=city,
                    state=state,
                    country=country,
                    auth_token=auth_token
                    )
                user_obj.set_password(password)
                user_obj.save()
                print(auth_token) 
                sendMailAfterRagistration(email, auth_token)
                return redirect("/sendmail") 
            except Exception as e:
                print(e)
        context['register_form'] = form
    else:
        form = SignUpForm()
        context['register_form'] = form
    return render(request, "register.html", context)


def sendMailAfterRagistration(email, token):
    subject = "Your account need to be verified"
    message = f'Hi! click the link to verify your account http://127.0.0.1:8000/verified/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def verifiedView(request, auth_token):
    try:
        profile_obj = UserProfile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login')
        else:
            return redirect('error')
    
    except Exception:
        print(Exception)


def send_mail_view(request):
    return render(request, "sendmail.html")

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
            return redirect('/studenthome')
        elif user.user_type == "Teacher":
            login(request, user)
            return redirect('/teacherhome')
        elif user.user_type == "Parent":
            login(request, user)
            return redirect('/parenthome')

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