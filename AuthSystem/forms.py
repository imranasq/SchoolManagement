from .models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('email','password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Email or Password")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder' : 'email'}))
    username = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'username'}))
    first_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(max_length=50,  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Last Name'}))
    phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Phone'}))
    city = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'city'}))
    state = forms.CharField(max_length=50,  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'state'}))
    country = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'country'}))
    
    class Meta:
        model = UserProfile
        fields = ('email','username','first_name','last_name','phone','password1','password2', 'city', 'state', 'country')

       
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

