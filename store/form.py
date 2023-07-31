#from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
 
class CustomUserForm(UserCreationForm):
 username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name','name':'fname'}))
 email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email','name':'email'}))
 password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'your password','name':'password1'}))
 password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password2','name':'password2'}))

 class Meta:
    model=User
    fields=['username','email','password1','password2']