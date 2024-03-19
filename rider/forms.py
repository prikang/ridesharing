from django import forms 
from django.forms import fields  
from .models import RiderRegister
from django.db import models  
class RiderRegisterForm(forms.Form):
    fullname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    dateOfBirth=forms.DateField()
    email=forms.EmailField(max_length=100)
    phoneNumber=forms.CharField(max_length=30)
    vehicleNumber=forms.CharField(max_length=30)
    licenseNumber=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())
    licenseImage=forms.ImageField()

