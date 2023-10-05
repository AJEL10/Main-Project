from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
def signin(request):
    return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')
def service(request):
    return render(request, 'service.html')
def blog(request):
    return render(request, 'blog.html')
def contactus(request):
    return render(request, 'contactus.html')
def location(request):
    return render(request, 'location.html')
def forgot(request):
    return render(request, 'forgot.html')






