from django.shortcuts import render
from .models import Task


def home(request):
    tasks = Task.objects.all().order_by('-created_at')

    context = {
        'app_name': 'Family Todo',
        'message': f'Pocet taskov v databaze: {tasks.count()}',
        'tasks': tasks,
    }

    return render(request, 'tasks/home.html', context)