from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Orphan, Guardian
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms



def home_page(request):
    return render(request,  'pages/home.html')

def about_page(request):
    return render(request,  'pages/about.html')

def orphan_page(request):
    orphan = Orphan.objects.all()  # Get all Orphan objects
    return render(request,  'pages/orphan.html', {'orphan': orphan})

def contact_page(request):
    return render(request,  'pages/contacts.html')

def adminpanel_page(request):
    return render(request,  'pages/adminpanel.html')


# Home page
def index(request):
    return render(request, 'index.html')


# login page
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("You have been logged in."))
			return redirect('HomePage')
		else:
			messages.success(request, ("There is an error, please try again."))
			return redirect('LogPage')
	else:
		return render(request, 'pages/login.html')

# logout page
def user_logout(request):
	logout(request)
	messages.success(request, ("You have been logget out."))
	return redirect('HomePage')

def adminpanel_page(request):
      employee = Guardian.objects.all()
      context = {
            'employee':employee,
      }
      return render(request, 'pages/adminpanel.html', context)

def add_orphan(request):
    form = OrphanForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('OrphanPage')
    return render(request, 'pages/add_orphan.html',{'form':form})

def edit_orphan(request, pk):
    orphan = Orphan.objects.get(id=pk)
    form = OrphanForm(request.POST or None, instance=orphan)
    if form.is_valid():
        form.save()
        return redirect('OrphanPage')

    return render(request, 'pages/edit_orphan.html', {'orphan':orphan, 'form': form})

def delete_orphan(request, pk):
    orphan = Orphan.objects.get(id=pk)
    orphan.delete()
    return redirect('OrphanPage')
pass

def view_orphan(request, pk):
    orphan = Orphan.objects.get(id=pk)

    return render(request, 'pages/view_orphan.html', {'orphan': orphan})



def add_guardian(request):
    form = GuardianForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('AdminPanel')
    return render(request, 'pages/add_guardian.html',{'form':form})

def edit_guardian(request, pk):
    guardian = Guardian.objects.get(id=pk)
    form = GuardianForm(request.POST or None, instance=guardian)
    if form.is_valid():
        form.save()
        return redirect('AdminPanel')

    return render(request, 'pages/edit_guardian.html', {'guardian':guardian, 'form': form})

def delete_guardian(request, pk):
    guardian = Guardian.objects.get(id=pk)
    guardian.delete()
    return redirect('AdminPanel')
pass