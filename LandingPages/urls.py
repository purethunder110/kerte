from django.urls import path
from .views import *

urlpatterns=[
    path('',landingPage,name="landingpage"),
    path('home/',Homepage,name="homepage"),
    path('@post/new',remainingurl),
    path('@post/edit/<int:postid>',remainingurl),
    path('@post/view/<int:postid>',remainingurl),
]