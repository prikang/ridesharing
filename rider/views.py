from django.shortcuts import render,redirect
from django.db import IntegrityError, transaction
from django.http import HttpResponse
from rider.models import RiderRegister
from rider.forms import RiderRegisterForm
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
User=get_user_model()

def rider_register(request):
    form=RiderRegisterForm
    context={
        "form":form
    }
    return render(request,"rider_register.html",context=context)

def save_rider_register(request):
    if request.method=="POST":
        form=RiderRegisterForm(data=request.POST)
        form.is_valid()
        data= form.cleaned_data
        # try:
        with transaction.atomic():
            user=User.objects.create(
                
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password")

            )

            RiderRegister.objects.create(
                fullname=data.get("fullname"),
                dateOfBirth=data.get("dateOfBirth"),
                phoneNumber=data.get("phoneNumber"),
                licenseNumber=data.get("licenseNumber"),
                vehicleNumber=data.get("vehicleNumber"),
                user=user
            )
        user.set_password(data.get("password"))
        user.save()
        messages.success(request,"User register successfully")
        # except IntegrityError:
        #     messages.error(request,"User with this username already exist")
        
    return redirect("login_view")
    
def home_page(request):
    return HttpResponse("This is home page")