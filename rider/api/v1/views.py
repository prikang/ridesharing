from rest_framework.response import Response
from rest_framework.views import APIView
from rider.models import RiderRegister
from rider.models import PassengerOnRide
from .serializers import RiderSerializer
from .serializers import UserSerializer
from .serializers import PassengerOnRideSerializer
from django.contrib.auth import get_user_model

User=get_user_model()
class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        queryset= RiderRegister.objects.all()
        serializer=RiderSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        file = request.FILES.get('liscenseImage')
        serializer=RiderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['file'] = file

        print(serializer.validated_data)
        serializer.save()
        return Response({"message":"Data saved"})
    
class UserAPIView(APIView):
    def get(self,request,*args,**kwargs):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)

class PassengerOnRideAPIView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=PassengerOnRideSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        PassengerOnRide.objects.create(
            from_location=data.get("from_location"),
            to=data.get("to"),
            rider=data.get("rider"),
            passenger=data.get("passenger")
        )
        print(serializer.validated_data)
        serializer.save()
        return Response({"message":"Data saved"})

        
