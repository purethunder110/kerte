from django.shortcuts import render,HttpResponse

# Create your views here.

def firstpage(request):
    return HttpResponse("everything works")