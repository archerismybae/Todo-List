from .models import TodoListItem
from django import forms
from django.forms import ModelForm

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoListItem
        fields = ['content']
        labels = {
            'content': 'Add task'
        }