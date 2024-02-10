from django.shortcuts import render,HttpResponse

# Create your views here.

def Homepage(request):
    return render(request,"html/landingPage.html")


#@login_required(login_url="/login")
def NewPost(request):
    return render(request,"html/post.html")


def landingPage(request):
    return render(request,"html/Homepage.html")

def remainingurl(response):
    return HttpResponse("<h1>page getting ready")