from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def signupage(request):
    if request.method=="GET":
        return render(request,"html/signup.html")
    if request.method=="POST":
        if "SignupDetails" in request.POST:
            name=request.POST.get("username")
            password=request.POST.get("password")
            email=request.POST.get("email")
            userRegister=User.objects.create_user(username=name,password=password,email=email)
            userRegister.save()
        return render(request,"html/signup.html")

def signinpage(request):
    if request.method=="GET":
        return render(request,"html/signin.html")
    if request.method=="POST":
        if "username" in request.POST:
            name=request.POST.get("username")
            password=request.POST.get("password")
            user_auth=authenticate(username=name,password=password)
            if user_auth:
                print("asa")
                login(request,user_auth)
                return redirect("/newpost")
            else:
                print("asad")
                return redirect("/err")
        else:
            return redirect("/err")

def remainingurl(response):
    return HttpResponse("<h1>page getting ready")