from django.urls import path
from .import views as v


urlpatterns = [
    path('', v.todo_list, name='todo_list'),
    path('todo/<int:id>/', v.todo_detail, name='todo_detail'),
    path('todo/add/', v.todo_add, name='todo_add'),
    path('todo/<int:id>/edit/', v.todo_edit, name='todo_edit'),
    path('todo/<int:id>/delete/', v.todo_delete, name='todo_delete'),
]
