from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import InputItemForm
from django.contrib.auth import authenticate, login, logout
from django.views import View

def home(request):
    print ("ASDDhsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd")
    context={}
    return render(request, 'base/home.html', context)
