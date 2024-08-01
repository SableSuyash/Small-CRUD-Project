from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    return render(request, 'todo_detail.html', {'todo': todo})

def todo_add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})

def todo_edit(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_form.html', {'form': form})

def todo_delete(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_confirm_delete.html', {'todo': todo})
