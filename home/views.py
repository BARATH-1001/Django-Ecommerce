from django.shortcuts import render,redirect
from django.http import HttpResponse,request

def hel(request):
   #return redirect("https://www.djangoproject.com") 
   return render(request,'front.html')

def index(request):
    return HttpResponse("you are connected to the webpage index")

def https(request):
    return render(request,"front copy.html")

def http(request):
    return render(request,"front copy 2.html")