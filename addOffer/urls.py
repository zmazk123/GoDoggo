from django.urls import path
from . import views

urlpatterns = [
    path("addOffer", views.addOffer, name="addOffer"),
]
