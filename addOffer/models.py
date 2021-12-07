from django.db import models
import pyrebase

import datetime
import json

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
auth = firebase.auth()
database = firebase.database()


class Offer:
    date = models.CharField(max_length=200)
    dog = models.CharField(max_length=200)
    uuid = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)

    def __init__(self):
        self.date = ""
        self.dog = ""
        self.uuid = ""
        self.location = ""
        
    def __init__(self, date, dog, uuid, location):
        self.date = date
        self.dog = dog
        self.uuid = uuid
        self.location = location

    def create(self):
        data = {"date": self.date, "dog": self.dog, "uuid": self.uuid, "location": self.location}
        database.child("Offers").push(data)

    @staticmethod
    def getEntries():
        return database.child("Offers").get().val()
