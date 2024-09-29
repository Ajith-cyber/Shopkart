from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def initial(request):
    return render(request, "shop/initial.html")

def home(request):
    return render(request, "shop/index.html")

def register(request):
    return render(request, "shop/register.html")


