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


class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)

class Offer:
    date = models.DateField()
    dogName = models.CharField(max_length=200)

    def __init__(self):
        self.date = ""
        self.dogName = ""
        
    def __init__(self, date, dogName):
        self.date = date
        self.dogName = dogName

    def create(self):
        data = {"date": self.date, "dogName": self.dogName}
        print(json.dumps(data,cls=DateTimeEncoder))
        database.child("Offers").push(json.dumps(data,cls=DateTimeEncoder))

    @staticmethod
    def getEntries():
        return database.child("Offers").get().val()
