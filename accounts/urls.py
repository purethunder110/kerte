from django.urls import path
from .views import *

urlpatterns=[
    path('signup/', signupage,name="signup"),
    path('signin/',signinpage),
    path('oauth/',twofactorauth),
    path('Reset/',remainingurl),
    path('delete/',remainingurl),
    path('details/',remainingurl), 
    path('profile/',remainingurl),
    path('logout/',logoutsite),
]