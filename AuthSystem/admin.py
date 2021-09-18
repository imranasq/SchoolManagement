from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from AuthSystem.models import UserProfile


# Register your models here.
admin.site.register(UserProfile)