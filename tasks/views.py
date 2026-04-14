from django.shortcuts import render
from .models import Task


def home(request):
    tasks = Task.objects.all().order_by('-created_at')

    context = {
        'app_name': 'FamilyToDo',
        'message': 'Welcome to FamilyToDo',
        'tasks': ['Task 1', 'Task 2', 'Task 3'],
    }
    return render(request, 'tasks/home.html', context)

