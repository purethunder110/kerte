from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import re
from django.http import JsonResponse
from .models import *
#sanitising post data
from nh3 import ALLOWED_ATTRIBUTES,ALLOWED_TAGS,clean


def Homepage(request):
    #All_user_joined_community=community_user_group.objects.filter(user=request.user)
    community_sidebar=community_user_group.objects.filter(user=request.user)
    All_posts=NewPost.objects.filter(User=request.user)
    paginator=Paginator(All_posts,12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    data={
        'channel_name':"Profile",
        'community_sidebar':community_sidebar,
        'posts':list(page_obj),
        'has_next':page_obj.has_next(),
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None
    }
    return render(request,"html/profilepage.html",data)

def loadProfileData(response):
    posts=NewPost.objects.filter(User=response.user)
    paginator=Paginator(posts,5)
    page_number=response.GET.get('page')
    print(page_number)
    page_obj=paginator.get_page(page_number)
    data = {
        'posts': list({
            'title':post.title,
            'postid':post.uuid,
            'description':post.description,
            'Community_name':post.Community.name,
            'Community_id':post.Community.uuid,
            'date':post.dateofpost,
        }for post in page_obj),
        'has_next': page_obj.has_next(),
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None
    }
    return JsonResponse(data)



#@login_required(login_url="/login")
def NewPostPage(request,communityid):
    community_object=Community.objects.get(uuid=communityid)
    all_tags=tags.objects.filter(Community=community_object)
    data={
        "Tags":all_tags,
    }
    if request.method=="GET":
        return render(request,"post.html",data)
    if request.method=="POST":
        heading=request.POST.get("heading")
        description=request.POST.get("description")
        Tag_select=tags.objects.get(uuid=request.POST.get("Tag_select"))
        body_post=request.POST.get("data")
        restricted=community_object.restricted
        print(request.POST.get("Tag_select"),restricted)
        create_post=NewPost(
            User=request.user,
            title=heading,
            description=description,
            Community=community_object,
            tags=Tag_select,
            restricted=restricted,
            body=body_post,
                            )
        create_post.save()
        return redirect("/@community/"+str(communityid))

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

def communityPosts(response,communityid):
    commun=Community.objects.get(uuid=communityid)
    posts=NewPost.objects.filter(Community=commun)
    paginator=Paginator(posts,5)
    page_number=response.GET.get('page')
    print(page_number)
    page_obj=paginator.get_page(page_number)
    data = {
        'posts': list({
            'title':post.title,
            'postid':post.uuid,
            'postuser':post.User.username,
            'description':post.description,
            'Community_id':post.Community.uuid,
            'date':post.dateofpost,
        }for post in page_obj),
        'has_next': page_obj.has_next(),
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None
    }
    return JsonResponse(data)

def searchpage(response,search):
    community_sidebar=community_user_group.objects.filter(user=response.user)
    data={
        'search':search,
        'channel_name':"Search Term:"+search,
        'community_sidebar':community_sidebar,
    }
    return render(response,"html/searchpage.html",data)

def SearchCommunity(request,search):
    Communitys=Community.objects.filter(name__icontains=search)
    for i in Communitys:
        print(i.name)
    print("finish")
    paginator=Paginator(Communitys,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    data = {
        'Community': list({
            'title':Community.name,
            'Communityid':Community.uuid,
            'description':Community.description,
        }for Community in page_obj),
        'has_next': page_obj.has_next(),
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None
    }
    print(data)
    return JsonResponse(data)


def UpdateCommunity(request,communityid):
    community_object=Community.objects.get(uuid=communityid)
    name=community_object.name
    description=communityid.description
    content={
        "community_header":"Make edits to Community"
        }
    return render(request,'create_community.html',content)

@login_required(login_url="/accounts/signin",redirect_field_name=None)
def joinCommunity(response,communityid):
    community=Community.objects.get(uuid=communityid)
    new_join=community_user_group(community=community,user=response.user,designation="USER")
    new_join.save()
    return redirect("/@community/"+str(communityid))

def leaveCommunity(response,communityid):
    community_object=Community.objects.get(uuid=communityid)
    join_instance=community_user_group.objects.filter(user=response.user,community=communityid)
    join_instance.delete()
    return redirect("/@community/"+str(communityid))

def ViewPostPage(request,postid):
    post_data=NewPost.objects.get(uuid=postid)
    community_sidebar=community_user_group.objects.filter(user=request.user)
    data={
        'community_sidebar':community_sidebar,
        "post_data":post_data,
    }
    return render(request,"html/single-post.html",data)

def editpost(request,postid):
    post_data=NewPost.objects.get(uuid=postid)
    all_tags=tags.objects.filter(Community=post_data.Community)
    data={
        "Tags":all_tags,
        "post_data":post_data,
    }
    if request.method=="GET":
        return render(request,"post.html",data)
    if request.method=="POST":
        heading=request.POST.get("heading")
        description=request.POST.get("description")
        body_post=request.POST.get("data")
        post_data.title=heading
        post_data.description=description
        print(body_post)
        post_data.body=body_post
        post_data.save()
        return redirect("/@post/view/"+str(post_data.uuid))




def DeletePost(response,postid):
    post_object=NewPost.objects.get(uuid=postid)
    post_object.delete()
    return redirect("/home/")

@login_required(login_url="/accounts/signin",redirect_field_name=None)
def ViewCommunity(request,communityid):
    community_sidebar=community_user_group.objects.filter(user=request.user)
    community_object=Community.objects.get(uuid=communityid)
    try:
        current_community_role=community_user_group.objects.get(community=community_object,user=request.user)
        designation=current_community_role.designation
    except:
        designation="New"
    All_posts=NewPost.objects.filter(Community=community_object).order_by('-dateofpost')
    paginator=Paginator(All_posts,20)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    community_Tags=tags.objects.filter(Community=community_object)
    data={
        'designation':designation,
        'community_sidebar':community_sidebar,
        'community_tags':community_Tags,
        'channel_name':community_object.name,
        'channel_id':community_object.uuid,
        'channel_description':community_object.description,
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



def modmanage(request,communityid):
    community_sidebar=community_user_group.objects.filter(user=request.user)
    community_object=Community.objects.get(uuid=communityid)
    current_community_role=community_user_group.objects.get(community=community_object,user=request.user)
    designation=current_community_role.designation
    community_user_list=community_user_group.objects.filter(community=community_object)
    data={
        'designation':designation,
        'community_sidebar':community_sidebar,
        'channel_name':"Manage Mod",
        'channel_id':community_object.uuid,
        'community_list':community_user_list,
    }
    if request.method=="GET":
        return render(request,"html/moderator.html",data)
    if request.method=="POST":
        user_uuid=request.POST.get("user_uuid")
        user_object=get_user_model()
        user_change_designation=user_object.objects.get(uuid=user_uuid)
        role_set=request.POST.get("role")
        if designation=="OWNER" or designation=="ADMIN":
            change_role=community_user_group.objects.get(community=community_object,user=user_change_designation)
            change_role.designation=role_set
            change_role.save()
        return render(request,"html/moderator.html",data)

def landingPage(request):
    return render(request,"html/Homepage.html")

def remainingurl(response):
    return HttpResponse("<h1>page getting ready")