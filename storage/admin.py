from django.contrib import admin
from .models import Room, Rack, Shelf

# Register your models here.
admin.site.register(Room)
admin.site.register(Rack)
admin.site.register(Shelf)