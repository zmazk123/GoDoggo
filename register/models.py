from django.db import models
import pyrebase
from requests.exceptions import HTTPError
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

class User(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __init__(self):
        self.email = ""
        self.password = ""
        
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def create(self):
        try:
            user = auth.create_user_with_email_and_password(self.email, self.password)
        except HTTPError as e:
            error = json.loads(e.strerror)
            raise Exception(error['error']['message'])

        uuid = user['localId']
        return uuid

    @staticmethod
    def authenticate(email, password):
        try:
            auth.sign_in_with_email_and_password(email, password)
        except HTTPError as e:
            error = json.loads(e.strerror)
            raise Exception(error['error']['message'])

        uuid = auth.current_user['localId']
        return uuid