from django.shortcuts import render
from .models import blogapp
# Create your views here.

def home(request) : 
    blogs = blogapp.objects
    return render(request, 'home.html',{'blog' : blogs})