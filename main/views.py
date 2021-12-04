from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from main.models import Dog
from .forms import CreateNewDog

def index(response):
    return render(response, "main/home.html")

def createDog(request):
    if request.method == "POST":
        form = CreateNewDog(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            breed = form.cleaned_data["breed"]
            age = form.cleaned_data["age"]
            description = form.cleaned_data["description"]
            uuid = request.session["uuid"]
            newDog = Dog(name, breed, age, description, uuid)
            newDog.save()

        return HttpResponseRedirect("/")


    form = CreateNewDog()
    return render(request, "main/createDog.html", {"form": form})