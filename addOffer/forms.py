from django import forms

class AddOfferForm(forms.Form):
    date = forms.DateTimeField(required="true")
    dogName = forms.CharField()
