from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class':'w-full p-2 border rounded'}))    
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'','class':'w-full p-2 border rounded'}))    
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'','class':'w-full p-2 border rounded'}))    
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'','class':'w-full p-2 border rounded'}))    

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class':'w-full p-2 border rounded'}))    
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'','class':'w-full p-2 border rounded'}))    

