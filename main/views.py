from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

def index(request):
    uuid = request.session["uuid"]
    currentUserDogs = Dog.getDogs(uuid)
    return render(request, "main/home.html", {"currentUserDogs": currentUserDogs})

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()

        return HttpResponseRedirect("/")


    form = CreateNewDog()
    return render(request, "main/createDog.html", {"form": form})

def viewDog(request, dogUid):
    if request.method == "POST":
        Dog.removeDogWithUid(dogUid)
        return HttpResponseRedirect("/")

    dog = Dog.getDogWithUid(dogUid)
    return render(request, 'main/viewDog.html', {'dog': dog })

def updateDog(request, dogUid):
    if request.method == "POST":
        form = CreateNewDog(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            breed = form.cleaned_data["breed"]
            age = form.cleaned_data["age"]
            description = form.cleaned_data["description"]
            uuid = request.session["uuid"]
            dog = Dog(name, breed, age, description, uuid)
            dog.updateDogWithUid(dogUid)

        return HttpResponseRedirect("/")

    dog = Dog.getDogWithUid(dogUid)
    form = CreateNewDog(initial={'name': dog['name'], 'breed': dog['breed'], 'age': dog['age'], 'description': dog['description']})
    return render(request, 'main/updateDog.html', {"form": form})
    