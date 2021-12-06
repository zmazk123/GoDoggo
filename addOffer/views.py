from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddOfferForm
from .models import Offer

import pyrebase
from pyrebase.pyrebase import Database

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

def addOffer(request):
    if request.method == "POST":
        form = AddOfferForm(request.POST)
        if form.is_valid():     
            date = form.cleaned_data["date"]
            dogName = form.cleaned_data["dogName"]
            offer = Offer(date, dogName)
            offer.create()
        return HttpResponseRedirect("/")

    allOffers = Offer.getEntries()

    form = AddOfferForm()
    return render(request, "addOffer/addOffer.html", {"entries":allOffers, "form":form})
