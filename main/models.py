from django.db import models

# Create your models here.

firebase = pyrebase.initialize_app(config)
database = firebase.database()
auth = firebase.auth()

class Dog(models.Model):
    name = models.CharField(max_length = 200)
    breed = models.CharField(max_length = 200)
    age = models.IntegerField()
    description = models.CharField(max_length = 2000, default="")
    uuid = models.CharField(max_length = 200)

    def __init__(self):
        self.name = ""
        self.breed = ""
        self.age = ""
        self.description = ""
        self.uuid = ""
        
    def __init__(self, name, breed, age, description, uuid):
        self.name = name
        self.breed = breed
        self.age = age
        self.description = description
        self.uuid = uuid

    def save(self):
        data = {"name": self.name, "breed": self.breed, "age": self.age, "description": self.description, "uuid": self.uuid}
        database.child("Dogs").push(data)

    @staticmethod
    def getDogs(currentUserUUID):
        return database.child("Dogs").order_by_child('uuid').equal_to(currentUserUUID).get().val()

    @staticmethod
    def getDogWithUid(uid):
        return database.child("Dogs").order_by_key().equal_to(uid).get().val()[uid]

    @staticmethod
    def removeDogWithUid(uid):
        database.child("Dogs").child(uid).remove()
        
    def updateDogWithUid(self, uid):
        data = {"name": self.name, "breed": self.breed, "age": self.age, "description": self.description, "uuid": self.uuid}
        database.child("Dogs").child(uid).update(data)