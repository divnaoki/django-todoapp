from django.shortcuts import render
from .models import TodoItem

# Create your views here.

def index(request):
  todo_list = TodoItem.objects.all()
  context = {'todo_list': todo_list}
  return render(request, 'todoapp/index.html', context)