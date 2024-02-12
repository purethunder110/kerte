from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.


def contactUs(request):
    return render(request,"html/contact.html")

def err(request):
    return render(request,"html/error page.html")