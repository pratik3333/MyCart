from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from .forms import RegistrationForm

# Create your views here.
def index(request):
    dest1 = Destination()

    return render(request,"shop/index.html",{'dest1:dest1'})

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at trackingstatus")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at productView")

def checkout(request):
    return HttpResponse("We are at checkout")
