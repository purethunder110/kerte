from django.urls import path
from .views import *

urlpatterns=[
    path('',landingPage,name="landingpage"),
    path('home/',Homepage,name="homepage"),
    path('@post/new',remainingurl),
    path('@post/edit/<uuid:postid>',remainingurl),
    path('@post/view/<uuid:postid>',remainingurl),
]