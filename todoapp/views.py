from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

# Create your views here.

def index(request):
  todo_list = TodoItem.objects.all()
  context = {'todo_list': todo_list}
  return render(request, 'todoapp/index.html', context)

def craete_todo(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      title = form.cleaned_data['title']
      new_item = TodoItem(title=title)
      new_item.save()
      return redirect('index')
  else:
    form = TodoForm()
  return render(request, 'todoapp/add.html', {'form': form})