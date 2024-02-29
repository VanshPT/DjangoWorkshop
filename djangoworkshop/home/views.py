from django.shortcuts import render
import requests
from .models import Basic
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        basic=Basic(name=name, email=email)
        basic.save()
    
    return render(request,'index.html')


def data(request):
    basic=Basic.objects.all()
    for name in basic:
        print(name.name)
    return render(request, 'getdata.html' , {'data':basic})