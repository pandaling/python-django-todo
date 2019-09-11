from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
	path('', views.index, name='index'),
	path('todolist/', views.addTodo, name='addTodo'),
	path('todolist/markascomplete/<int:item_id>', views.markAsComplete, name='markAsComplete'),
	path('todolist/deleteTodoItem/<int:item_id>', views.deleteTodoItem, name='deleteTodoItem'),
]