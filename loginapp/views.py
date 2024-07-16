from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventDetailsForm
from .models import PoornimaEventDetail

def homePage(request):
    return render(request,"homePage.html")

def login(request):
    if request.method=="POST":
        print("posted")
        name=request.POST['your first name']
        email=request.POST['email']
        print(name,email)
    return render(request,"Login.html")

def signup(request):
    # return render(request,"signup.html")
    if request.method == "post":
        firstname = request.POST['your first name']
        lastname = request.POST['your last name']
        email = request.POST['email']
        contact = request.POST['contact']
        data = PoornimaEventDetail()
    else:
        return render(request,"signup.html")
    return render(request,"Login.html")
    
    

