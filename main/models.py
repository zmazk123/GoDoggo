from django.db import models
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
database = firebase.database()

class Entry(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __init__(self):
        self.name = ""
        self.surname = ""
        
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def save(self):
        data = {"name": self.name, "surname": self.surname}
        database.child("Entries").push(data)

    @staticmethod
    def getEntries():
        return database.child("Entries").get().val()
