from rest_framework import serializers
from rider.models import RiderRegister
from rider.models import PassengerOnRide
from django.contrib.auth import get_user_model

User=get_user_model()

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model=RiderRegister 
        exclude = ('licenseImage',)
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class PassengerOnRideSerializer(serializers.ModelSerializer):
    class Meta:
        model=PassengerOnRide
        fields="__all__"


    