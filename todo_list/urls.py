from django.urls import path
from todo_list.views import home, enter_task, delete_items

urlpatterns = [
    path('', home, name = 'home'),
    path('form/', enter_task, name = 'form'),
    path('delete/<int:item>/', delete_items, name = 'delete' )
]