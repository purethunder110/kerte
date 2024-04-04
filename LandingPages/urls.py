from django.urls import path
from .views import *

urlpatterns=[
    path('',landingPage,name="landingpage"),
    path('home/',Homepage,name="homepage"),
    path('@post/new/<uuid:communityid>/',NewPostPage),
    path('@post/edit/<uuid:postid>',editpost),
    path('@post/view/<uuid:postid>',ViewPostPage),
    path('@post/delete/<uuid:postid>',DeletePost),
    path('@community/create',NewCommunity),
    path('@community/join/<uuid:communityid>',joinCommunity),
    path('@community/leave/<uuid:communityid>',leaveCommunity),
    path('@community/edit/<uuid:communityid>',UpdateCommunity),
    path('@community/<uuid:communityid>',ViewCommunity),
    path('@community/perms/<uuid:communityid>',modmanage),
]