from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

def Homepage(request):
    return HttpResponse("everything works")

def signup(request):
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

def loginpage(request):
    if request.method=="GET":
        return render(request,"login.html")
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

def contactUs(request):
    return render(request,"html/contact.html")

#@login_required(login_url="/login")
def NewPost(request):
    return render(request,"html/post.html")

def err(request):
    return HttpResponse("<h1>Internal error occured</h1>")