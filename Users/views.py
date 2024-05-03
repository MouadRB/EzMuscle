from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homepage(request):
    return render(request,'Users/Home.html')

def signup(request):
    return HttpResponse('')

def login(request):
    return HttpResponse('')

def userprofile(request,user_id):
    return HttpResponse('')

def editprofile(request,user_id):
    return HttpResponse('')
# Create your views here.
