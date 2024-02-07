from django import path
from .views import *

urlpatterns=[
    path(''),
    path('home/'),
    path('@post/new'),
    path('@post/edit/<int:postid>'),
    path('@post/view/<int:postid>'),
    path()
]