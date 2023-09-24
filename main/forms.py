from django.forms import ModelForm
from django import forms
from main.models import Animal

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ["name", "amount", "family", "animal_class", "description", "animal_image"]

class AnimalAmountForm(forms.Form):
    action = forms.CharField(max_length=10)
    animal_id = forms.IntegerField()