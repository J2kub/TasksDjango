from django.shortcuts import render


def home(request):
    context = {
        'app_name': 'FamilyToDo',
        'message': 'Welcome to FamilyToDo',
        'tasks': ['Task 1', 'Task 2', 'Task 3'],
    }
    return render(request, 'tasks/home.html', context)

