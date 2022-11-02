from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput(attrs={'id':'login-username','placeholder':'Username'}))  
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'id':'login-pass1','placeholder':'Password'}))  

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput(attrs={'id':'login-username','placeholder':'Username'}))  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'id':'login-pass1','placeholder':'Password'}))  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'id':'login-pass2','placeholder':'Confirm Password'}))  

  

    
