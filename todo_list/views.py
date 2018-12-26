from django.shortcuts import render, redirect
from .forms import ListForm
from .models import List
from django.contrib import messages

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST)

		if form.is_valid():
			form.save()
			all_items = List.objects.all()
			messages.success(request , ('Item has been added to the List!'))
			return render(request,'home.html', {'all_items' : all_items})
	else:
		all_items = List.objects.all()
		return render(request,'home.html', {'all_items' : all_items})


def cross_off(request, list_id):

	all_items = List.objects.get(pk=list_id)
	all_items.completed = True 
	all_items.save()
	return redirect('todo-list')

def un_cross(request, list_id):

	all_items = List.objects.get(pk=list_id)
	all_items.completed = False
	all_items.save()
	return redirect('todo-list')

def delete(request, list_id):

	all_items = List.objects.get(pk=list_id)
	all_items.delete()
	messages.success(request,('item deleted'))
	return redirect('todo-list')

def edit(request, list_id):

	if request.method == 'POST':

		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST,instance=item )

		if form.is_valid():
			form.save()
			messages.success(request , ('Item has been Edited'))
			return redirect('todo-list')
	else:

		item = List.objects.get(pk=list_id)
		return render(request,'edit.html', {'item' : item})







