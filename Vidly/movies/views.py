from django.shortcuts import render
from django.http import HttpResponse
from . models import Genre

# Create your views here.

def index(request):
    genres = Genre.objects.all()

    return render(request, 'views/index.html', { 'title' : 'Index Page', 'items' : genres})

def catalog(request):
    return render(request, 'views/catalog.html')

def welcome(request):
    return render(request, 'views/welcome.html', { 'title' : 'Welcome', 'rows' : 2})

def about(request):
    return HttpResponse("<h1>about</h1><h2>My name is Adam Laston</h2>")