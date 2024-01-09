from django.shortcuts import render,HttpResponse

# Create your views here.

def firstpage(request):
    return HttpResponse("everything works")

def signup(request):
    return render(request,"html/signup.html")

def login(request):
    return render(request,"html/signin.html")

def contactUs(request):
    return render(request,"html/contact.html")

def NewPost(request):
    return render(request,"html/post.html")