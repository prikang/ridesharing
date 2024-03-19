from django.urls import path
from .views import pass_register,save_pass_register

urlpatterns = [
    path("pass_register",pass_register,name="pass_register"),
    path("save_pass_register",save_pass_register,name="save_pass_register")
]
