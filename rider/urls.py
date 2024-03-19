from django.urls import path
from .views import rider_register,save_rider_register,home_page

urlpatterns = [
    path("rider_register",rider_register,name="rider_register"),
    path("save_rider_register",save_rider_register,name="save_rider_register"),
    path("home_page",home_page,name="home_page")
]
