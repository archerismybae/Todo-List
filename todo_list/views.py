from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoListItem
from .forms import TodoListForm

def home(request):
    context = {
        'items': TodoListItem.objects.all()
    }
    return render(request, 'home.html', context)

def enter_task(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Form not valid')
    else:
        form = TodoListForm(auto_id=False)
    return render(request, 'form.html', {'form': form})