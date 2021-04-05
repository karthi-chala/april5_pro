from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>welcome to index of app2</h1>')

def sample_app2(request):
    return render(request,'sample_app2.html')

# Create your views here.
