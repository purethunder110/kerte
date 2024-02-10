from django import path
from .views import *

urlpatterns=[
    path('signup/'),
    path('signin/'),
    path('Reset/'),
    path('delete/'),
    path('details/'), 
    path('profile/'),
]