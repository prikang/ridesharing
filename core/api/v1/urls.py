from django.urls import path
from .views import LocationAPIView


urlpatterns = [
    
    path("location/", LocationAPIView.as_view(), name="location-api-view")
    
]
