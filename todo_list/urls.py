from django.urls import path
from todo_list.views import home, enter_task

urlpatterns = [
    path('', home, name = 'home'),
    path('form/', enter_task, name = 'form')
]