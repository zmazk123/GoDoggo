from django import forms

class CreateNewDog(forms.Form):
    name = forms.CharField(label = "Name", max_length = 200)
    breed = forms.CharField(label = "Breed", max_length = 200)
    age = forms.IntegerField(label = "Age", widget=forms.NumberInput, max_value = 20, min_value = 1)
    description = forms.CharField(label = "Description", widget=forms.Textarea, required=False)
    