from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from PIL import Image
from io import BytesIO
# Create your views here.

def signupage(request):
    User=get_user_model()
    if request.method=="GET":
        return render(request,"html/signup.html")
    if request.method=="POST":
        if "SignupDetails" in request.POST:
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            Age=request.POST.get("Age")
            profile_pic=request.FILES.get("profile_pic")
            username=request.POST.get("username")
            password=request.POST.get("password")
            email=request.POST.get("email")
            #validation on the server side
            #is not empty
            if len(username)==0 or len(password)==0 or len(email)==0:
                return JsonResponse({
                    'error':'Required Field has invalid Value'
                    },status=406)
            #validate email
            try:
                validate_email(email)
            except ValidationError as e:
                return JsonResponse({
                    "error":"The Email is not valid"
                },status=406)
            #validate profile_pic
            try:
                profile=Image.open(profile_pic)
                #width and hight to be 300x300
                
                if profile.width>300 or profile.hight>300:
                    return JsonResponse({
                        'error':'Profile Picture should be in 300x300 resolution'
                    },status=406)
            except:#no profile pic provided, using default pic
                pass
            #registeration problem occurs
            
            try:
                print("registering")
                userRegister=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,Age=Age)
                userRegister.save()
                print("registered")
            except:
                auth_token=authenticate(email=email,password=password)
                if auth_token is not None:
                    return JsonResponse({
                        'error':'This email is already registered with a account '
                    },status=406)
                else:
                    return JsonResponse({'error':'internal server error while registering'},status=406)
        return render(request,"html/signup.html")

def signinpage(request):
    if request.method=="GET":
        return render(request,"html/signin.html")
    if request.method=="POST":
        if "LoginID" in request.POST:
            username=request.POST.get("LoginID")
            password=request.POST.get("password")
            user_auth=authenticate(username=username,password=password)
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

@login_required(login_url="/accounts/signin",redirect_field_name=None)
def logoutsite(request):
    logout(request)
    return redirect("/")

def remainingurl(response):
    return HttpResponse("<h1>page getting ready")