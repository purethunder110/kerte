from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login
from django.urls import reverse
# Create your views here.

def signupage(request):
    User=get_user_model()
    if request.method=="GET":
        return render(request,"html/signup.html")
    if request.method=="POST":
        if "SignupDetails" in request.POST:
            name=request.POST.get("username")
            password=request.POST.get("password")
            email=request.POST.get("email")
            userRegister=User.objects.create_user(username=name,password=password,email=email,first_name="temp",last_name="temp2",Age=18)
            userRegister.save()
        return render(request,"html/signup.html")

def signinpage(request):
    if request.method=="GET":
        return render(request,"html/signin.html")
    if request.method=="POST":
        if "LoginID" in request.POST:
            email=request.POST.get("LoginID")
            password=request.POST.get("password")
            user_auth=authenticate(email=email,password=password)
            print("this is auth",user_auth)
            if user_auth is not None:
                print("test1")
                login(request,user_auth)
                return redirect("/home")
            else:
                print(user_auth)
                return redirect("/err")
        else:
            print("test1")
            return redirect("/err")

def remainingurl(response):
    return HttpResponse("<h1>page getting ready")