from django.shortcuts import render,redirect
from django.db import IntegrityError, transaction
from django.http import HttpResponse
from passenger.models import PassRegister
from passenger.forms import PassRegisterForm
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
User=get_user_model()

def pass_register(request):
    form=PassRegisterForm
    context={
        "form":form
    }
    return render(request,"pass_register.html",context=context)

def save_pass_register(request):
    if request.method=="POST":
        form=PassRegisterForm(data=request.POST)
        form.is_valid()
        data= form.cleaned_data
        # try:
        with transaction.atomic():
            pass_user=User.objects.create(
                
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password")

            )

            PassRegister.objects.create(
                fullname=data.get("fullname"),
                dateOfBirth=data.get("dateOfBirth"),
                phoneNumber=data.get("phoneNumber"),
                pass_user=pass_user
            )
        pass_user.set_password(data.get("password"))
        pass_user.save()
        messages.success(request,"User register successfully")
        # except IntegrityError:
        #     messages.error(request,"User with this username already exist")
        
    return redirect("login_view")
