from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is Required")
        

        user=self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        user = self.create_user(
            email = email,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff= True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser):
    USER_CHOICES = (
    ('Admin', 'Admin'),
    ('Teacher', 'Teacher'),
    ('Parent', 'Parent'),
    ('Student','Student'),
    )
    email =models.EmailField(verbose_name="email address", max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    profile_pic = models.ImageField(null = True, blank = True, upload_to = 'images/')
    user_type = models.CharField(max_length=10,choices=USER_CHOICES,null=True,blank=False)
    phone = models.CharField(max_length=15, verbose_name="phone")
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD="email"

    #REQUIRED_FIELDS=['']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app__label):
        return True
