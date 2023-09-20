from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import AnimalForm
from main.models import Animal
from django.urls import reverse
from django.core import serializers

def show_main(request):
    animals = Animal.objects.all()
    animal_sum = 0
    for animal in animals:
        animal_sum += animal.amount

    context = {
        'name': 'Athira Reika', # Nama kamu
        'class': 'PBP F', # Kelas PBP kamu
        'animal_sum': animal_sum,
        'animals': animals
    }

    return render(request, "main.html", context)

def create_animal(request):
    form = AnimalForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_animal.html", context)

def show_xml(request):
    data = Animal.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Animal.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Animal.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Animal.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

