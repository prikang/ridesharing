from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Location
from .serializers import LocationSerializer


class LocationAPIView(APIView):
    def get(self,request,*args,**kwargs):
        queryset= Location.objects.all()
        serializer=LocationSerializer(queryset,many=True)

        return Response(serializer.data)

