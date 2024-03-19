from django.urls import path
from .views import TestAPIView
from .views import UserAPIView
from.views import PassengerOnRideAPIView

urlpatterns = [
    
    path("test/", TestAPIView.as_view(), name="test-api-view"),
    path("user/", UserAPIView.as_view(), name="user-api-view"),
    path("passenger/",PassengerOnRideAPIView.as_view(), name="passenger-api-view")

]
