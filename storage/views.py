from django.shortcuts import render, redirect
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def room_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Room.objects.create(name=name)
            return redirect('room_list')
    return render(request, 'room_create.html')