from django.forms import ModelForm
from main.models import Animal

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ["name", "amount", "family", "animal_class", "description", "animal_image"]