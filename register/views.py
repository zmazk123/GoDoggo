from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, LogInForm
from .models import User

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():     
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User(email, password)
            user.create()
            request.session['authenticated']="True"
        return HttpResponseRedirect("/")

    form = RegistrationForm()
    return render(request, "register/register.html", {"form": form})

def logIn(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():     
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.authenticate(email, password)
            request.session['authenticated']="True"
        return HttpResponseRedirect("/")

    form = LogInForm()
    return render(request, "register/logIn.html", {"form": form})

def logOut(request):
    request.session['authenticated']="False"
    return HttpResponseRedirect("/")