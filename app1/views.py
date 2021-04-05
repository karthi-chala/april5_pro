from django.shortcuts import render
import os
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>welcome to index of app1</h1>')

def sample_app1(request):
    return render(request,'sample_app1.html')