import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from main.forms import AnimalForm, AnimalAmountForm
from main.models import Animal
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/login')
def show_main(request):
    animals = Animal.objects.filter(user=request.user)
    animal_sum = 0
    species_sum = animals.count
    for animal in animals:
        animal_sum += animal.amount
    user_authenticated = request.user.is_authenticated

    context = {
        'name': request.user.username,
        'class': 'PBP F',
        'species_sum': species_sum,
        'animal_sum': animal_sum,
        'animals': animals,
        'last_login': request.COOKIES['last_login'],
        'user_authenticated': user_authenticated
    }

    return render(request, "main.html", context)

def create_animal(request):
    form = AnimalForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.method == "POST":
        animal = form.save(commit=False)
        animal.user = request.user
        animal.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    context['user_authenticated']: user_authenticated
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

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def update_animal_amount(request):
    if request.method == 'POST':
        form = AnimalAmountForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            animal_id = form.cleaned_data['animal_id']
            animal = Animal.objects.get(id=animal_id)

            if action == 'increment':
                animal.amount += 1
                animal.save()
            elif action == 'decrement' and animal.amount > 0:
                animal.amount -= 1
                animal.save()
                if animal.amount == 0:
                    animal.delete()
            elif action == 'delete':
                animal.amount -= animal.amount
                if animal.amount == 0:
                    animal.delete()

    return redirect('main:show_main')

def get_animal_json(request):
    animal_item = Animal.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', animal_item))

@csrf_exempt
def add_animal_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        family = request.POST.get("family")
        animal_class = request.POST.get("animal_class")
        description = request.POST.get("description")
        animal_image = request.POST.get("animal_image")
        user = request.user

        new_animal = Animal(name=name, amount=amount, family=family, animal_class=animal_class, description=description, animal_image=animal_image, user=user)
        new_animal.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_animal_ajax(request, id):
    if request.method == 'DELETE':
        item = Animal.objects.get(pk=id)
        item.delete()
        return HttpResponse(b"DELETED", status=200)
    return HttpResponseNotFound()

@csrf_exempt
def create_animal_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_animal = Animal.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            family = data["family"],
            animal_class = data["animal_class"],
            description = data["description"]
        )

        new_animal.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)