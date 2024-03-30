from django.contrib.auth.models import User
from django import forms 
from django.contrib.auth.forms import UserCreationForm



        

# create the login the form
class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'username','id':'username1'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','id':'login-password1'}))