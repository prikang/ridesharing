from django.shortcuts import render, redirect
from authentication.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse

def login_view(request):
    form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context=context)

def save_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return redirect("home_page")  # Redirect to the home page upon successful login
            else:
                messages.error(request, "Wrong username or password")
        return redirect("login_view")  # Redirect to login_view if the form is invalid or authentication fails

def logout_view(request):
    logout(request)
    return redirect("login_view")
