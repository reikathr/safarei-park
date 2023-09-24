from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    family = models.CharField(max_length=255)
    animal_class = models.CharField(max_length=255, default='Mammalia')
    description = models.TextField()
    animal_image = models.ImageField(upload_to='images/',default='images/default.png')