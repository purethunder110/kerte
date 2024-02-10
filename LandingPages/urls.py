from django.urls import path
from .views import *

urlpatterns=[
    path('',Homepage,name="homepage"),
    path('home/',landingPage,name="landingpage"),
    path('@post/new',remainingurl),
    path('@post/edit/<int:postid>',remainingurl),
    path('@post/view/<int:postid>',remainingurl),
]