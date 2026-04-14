from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    tasks = Task.objects.all().order_by('-created_at')

    context = {
        'app_name': 'Family Todo',
        'message': 'Tasky nacitane z databazy cez Django ORM.',
        'tasks': tasks,
        'form': form,
    }

    return render(request, 'tasks/home.html', context)