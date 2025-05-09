from django.db import models
from django.contrib.auth.models import AbstractUser

# Room model
class Room(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

# Rack model
class Rack(models.Model):
    name = models.CharField(max_length=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Shelf model
class Shelf(models.Model):
    number = models.IntegerField()
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shelf {self.number} in Rack {self.rack.name}"
