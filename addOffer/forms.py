from django import forms

class AddOfferForm(forms.Form):
    date = forms.CharField()
    dogName = forms.CharField()
    location = forms.CharField()
