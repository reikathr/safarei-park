from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    family = models.CharField(max_length=255)
    animal_class = models.CharField(max_length=255, default='Mammalia')
    description = models.TextField()
    animal_image = models.ImageField(upload_to='images/',default='media/default.png')