from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Create your views here.
class RegisterUserForm(UserCreationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder' :'Användarnamn', 'style': 'width: 300px;', 'class': 'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Förnamn', 'style': 'width: 300px;', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Efternamn', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'E-postadress', 'style': 'width: 300px;', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Lösenord', 'style': 'width: 300px;', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Lösenord', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta : 
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')