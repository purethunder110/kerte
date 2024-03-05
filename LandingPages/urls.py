from django.urls import path
from .views import *

urlpatterns=[
    path('',landingPage,name="landingpage"),
    path('home/',Homepage,name="homepage"),
    path('@post/new/<uuid:communityid>',NewPostPage),
    path('@post/edit/<uuid:postid>',remainingurl),
    path('@post/view/<uuid:postid>',remainingurl),
    path('@community/create',NewCommunity),
    path('@community/edit/<uuid:communityid>',UpdateCommunity),
    path('@community/<uuid:communityid>',ViewCommunity),
]