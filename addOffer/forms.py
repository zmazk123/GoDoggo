from django import forms
from main.models import Dog

CHOICE_LIST= [
    ('aro', 'aro'),
    ('bobi', 'bobi'),
    ('megatron', 'megatron'),
    ('medo', 'medo'),
    ('Kapitan', 'Kapitan'),
    ]

class AddOfferForm(forms.Form):
    date = forms.CharField()
    dog = forms.CharField(widget=forms.Select(choices=CHOICE_LIST))
    location = forms.CharField()
