from django.urls import path
from .views import login_view
from .views import save_login
from .views import save_login
from .views import logout_view

urlpatterns = [
    path("login_view",login_view,name="login_view"),
    path("save_login",save_login,name="save_login"),
    path("logout",logout_view,name="logout")

]
