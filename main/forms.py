from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label = "Name", max_length = 200)
    surname = forms.CharField(label = "Surame", max_length = 200)