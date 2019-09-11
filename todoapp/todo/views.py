from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Todo
from django.utils import timezone

def index(request):
	todo_list = Todo.objects.all()
	context = { 'todo_list': todo_list }
	return render(request, 'todo/index.html', context)

def addTodo(request):
	add_todo = request.POST.get('add_todo_name', None)
	current_date = timezone.now()
	new_todo_item = Todo(item_name=add_todo, item_status="new", created_date=current_date)
	new_todo_item.save()
	return HttpResponseRedirect(reverse('todo:index'))

def markAsComplete(request, item_id):
	item = Todo.objects.get(pk=item_id)
	item.item_status = 'done'
	item.save()
	return HttpResponseRedirect(reverse('todo:index'))

def deleteTodoItem(request, item_id):
	print('delete: ', item_id)
	item = Todo.objects.get(pk=item_id)
	item.delete()
	return HttpResponseRedirect(reverse('todo:index'))