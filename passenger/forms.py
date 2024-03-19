from django import forms 
from django.forms import fields  
from .models import PassRegister
from django.db import models  
class PassRegisterForm(forms.Form):
    fullname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    dateOfBirth=forms.DateField()
    email=forms.EmailField(max_length=100)
    phoneNumber=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())
   
