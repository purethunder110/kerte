from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator
import re
from django.http import JsonResponse
from .models import Community,community_user_group,NewPost,tags
#sanitising post data
from nh3 import ALLOWED_ATTRIBUTES,ALLOWED_TAGS,clean


def Homepage(request):
    #All_user_joined_community=community_user_group.objects.filter(user=request.user)
    All_posts=NewPost.objects.filter(User=request.user)
    paginator=Paginator(All_posts,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    data={
        'channel_name':"Profile",
        'posts':list(page_obj),
        'has_next':page_obj.has_next(),
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None
    }
    return render(request,"html/profilepage.html",data)


#@login_required(login_url="/login")
def NewPostPage(request,communityid):
    community_object=Community.objects.get(uuid=communityid)
    all_tags=tags.objects.filter(Community=community_object)
    data={
        "Tags":all_tags
    }
    if request.method=="GET":
        return render(request,"html/post.html",data)
    if request.method=="POST":
        heading=request.POST.get("heading")
        description=request.POST.get("description")
        data=request.POST.get("data")
        return render(request,"html/post.html",data)

def NewCommunity(request):
    content={
        "community_header":"Create a new community"
        }
    if request.method=="GET":
        return render(request,'community.html',content)
    if request.method=="POST":
        if "Community_name" in request.POST:
            community=request.POST.get("Community_name")
            restricted=True if request.POST.get("restricted")=="true" else False
            description=request.POST.get("description")
            regex=r'^[a-zA-Z]{8,}$'
            if bool(re.match(regex,community)):
                #community registeration
                print("create community")
                new_community=Community(name=community,restricted=restricted,description=description,Owner=request.user)
                new_community.save()
                #user joining the community
                uuid=Community.objects.get(name=community)
                owner_register=community_user_group(community=uuid,user=request.user,designation="OWNER")
                owner_register.save()
                return redirect("/@community/"+str(uuid.get_uuid()))
            else:
                return JsonResponse({
                    'error':'please enter a name with no symbols and minimum 8 letters'
                },status=406)
            #return render(request,"community.html",content)


def UpdateCommunity(request,communityid):
    community_object=Community.objects.get(uuid=communityid)
    name=community_object.name
    description=communityid.description
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
    paginator=Paginator(All_posts,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    data={
        'channel_name':community_object.name,
        'posts':list(page_obj),
        'has_next':page_obj.has_next(),
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None
    }
    if request.method=="GET":
        return render(request,'html/landingPage.html',data)
    if request.method=="POST":
        tagname=request.POST.get("Tagname")
        tagdiscription=request.POST.get("Tagdescription")
        newTag=tags(Community=community_object,name=tagname,description=tagdiscription)
        newTag.save()
        return render(request,"html/landingPage.html",data)

def landingPage(request):
    return render(request,"html/Homepage.html")

def remainingurl(response):
    return HttpResponse("<h1>page getting ready")