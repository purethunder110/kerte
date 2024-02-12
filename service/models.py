from django.db import models
from django.contrib.auth.models import AbstractUser   
import uuid
from .managers import base_user_manager
# Create your models here.

class Base_user(AbstractUser):
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Age=models.IntegerField()
    profile_pic=models.ImageField(default="static/images/DefaultAvatar.jpg",upload_to="static/UserGenerated/profilepic")
    disabled=models.BooleanField(default=False)

    objects = base_user_manager()