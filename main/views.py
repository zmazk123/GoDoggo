from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from pyrebase.pyrebase import Database
from .forms import CreateNewList
from .models import Entry

config = {
    "apiKey": "AIzaSyAgaZYQDBNyfMNI3A7ocJB1DP_vHiUdo2o",
    "authDomain": "godoggo-a18ac.firebaseapp.com",
    "databaseURL": "https://godoggo-a18ac-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "godoggo-a18ac",
    "storageBucket": "godoggo-a18ac.appspot.com",
    "messagingSenderId": "929780314718",
    "appId": "1:929780314718:web:31b97491b560bc07dc7acf"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def index(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            newEntry = Entry(name, surname)
            newEntry.save()

    allEntries = Entry.getEntries()
    #entryOneName = allEntries['1']['name']
    form = CreateNewList()
    return render(response, "main/home.html", {"entries":allEntries, "form":form})