from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name="login"),
    path('home/', homeview, name="home"),
    path('logout/', logout_view, name = "logout"),
]