from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator
import re
from django.http import JsonResponse
from .models import Community,community_user_group
# Create your views here.

def Homepage(request):
    #All_user_joined_community=community_user_group.objects.filter(user=request.user)
    All_posts=NewPost.objects.filter(User=request.User)
    paginator=paginator(All_posts,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    data={
        'posts':list(page_obj),
        'has_next':page_obj.has_next(),
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None
    }
    return render(request,"html/profilepage.html")


#@login_required(login_url="/login")
def NewPost(request):
    return render(request,"html/post.html")

def NewCommunity(request):
    content={
        "community_header":"Create a new community"
        }
    if request.method=="GET":
        return render(request,'community.html',content)
    if request.method=="POST":
        if "Community_name" in request.POST:
            community=request.POST.get("Community_name")
            restricted=request.POST.get("restricted")
            description=request.POST.get("discription")
            regex=r'^[a-zA-Z]{8,}$'
            if bool(re.match(regex,community)):
                #community registeration
                new_community=Community(name=community,restricted=restricted,description=description,Owner=request.user)
                new_community.save()
                #user joining the community
                uuid=Community.objects.get(Community=community)
                owner_register=community_user_group(community=uuid,user=request.user,designation="OWNER")
                owner_register.save()
                return redirect("/home/"+uuid.get_uuid())
            else:
                return JsonResponse({
                    'error':'please enter a valid name'
                },status=406)
            return render(request,"community.html",content)


def UpdateCommunity(request,uuid):
    
    content={
        "community_header":"Make edits to Community"
        }
    return render(request,'create_community.html',content)

def joinCommunity(response,uuid):
    return JsonResponse({
        'success':"successfully added to community"
    },status=200)

def ViewCommunity(request,communityid):
    community_object=Community.objects.get(uuid=communityid)
    All_posts=NewPost.objects.filter(Community=community_object)
    paginator=paginator(All_posts,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    data={
        'posts':list(page_obj),
        'has_next':page_obj.has_next(),
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None
    }

    return render(request,'html/langingPage.html',data)

def landingPage(request):
    return render(request,"html/Homepage.html")

def remainingurl(response):
    return HttpResponse("<h1>page getting ready")