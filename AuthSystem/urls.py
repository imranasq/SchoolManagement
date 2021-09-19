from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('', indexView, name="index"),
    path('admin/', dashboard_view, name="dashboard"),
    path('studenthome/', studentHomeView, name="student-home"),
    path('teacherhome/', teacherHomeView, name="teacher-home"),
    path('parenthome/', parentHomeView, name="parent-home"),
    path('logout/', logout_view, name = "logout"),
]