from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createDog", views.createDog, name="createDog"),
    path('dogs/<str:dogUid>/', views.viewDog, name='viewDog'),
    path('dogs/<str:dogUid>/updateDog', views.updateDog, name='updateDog'),
]