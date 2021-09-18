from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name="login"),
    path('home/', homeview, name="home"),
    path('studenthome/', homeview, name="student-home"),
    path('logout/', logout_view, name = "logout"),
]