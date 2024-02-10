from django.urls import path
from .views import *

urlpatterns=[
    path('signup/', signupage,name="signup"),
    path('signin/',signinpage),
    path('Reset/',remainingurl),
    path('delete/',remainingurl),
    path('details/',remainingurl), 
    path('profile/',remainingurl),
]