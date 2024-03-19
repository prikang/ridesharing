from django.db import models
from core.models import Location
from passenger.models import PassRegister
from django.contrib.auth import get_user_model
# Create your models here.

user= get_user_model()
class RiderRegister(models.Model):
    user= models.OneToOneField(user,
                               related_name="rider",
                               on_delete=models.CASCADE)
    fullname=models.CharField(max_length=30)
    dateOfBirth=models.DateField()
    phoneNumber=models.CharField(max_length=50)
    vehicleNumber=models.CharField(max_length=30)
    licenseNumber=models.CharField(max_length=30)
    licenseImage=models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return f"{self.user.username}"

class PassengerOnRide(models.Model):
    from_location=models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name="from_location")
    to=models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name="to_location")
    passenger=models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name="passenger_on_rider")
    rider=models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name="rider_on_ride")
