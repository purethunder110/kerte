from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Extend_User(models.Model):
    User_object=models.ForeignKey(User,on_delete=models.CASCADE)
    Actuall_name=models.CharField(max_length=60)
    Age=models.IntegerField()
    profile_pic=models.ImageField()
    checkmark=models.IntegerField()
    premium=models.IntegerField()

class Community(models.Model):
    Owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name=models.CharField()
    description=models.TextField()

class tags(models.Model):
    Community=models.ForeignKey(Community,on_delete=models.DO_NOTHING)
    name=models.CharField(10)
    description=models.TextField()

class NewPost(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=100)
    crud_score=models.IntegerField(blank=True,null=True)
    Community=models.ForeignKey(Community,on_delete=models.DO_NOTHING,blank=True,null=True)
    tags=models.ForeignKey(tags,on_delete=models.DO_NOTHING,blank=True,null=True)
    restricted=models.BooleanField(default=False)
    archived=models.BooleanField(default=True)
    body=models.TextField()
    Upvote=models.IntegerField()
    Downvote=models.IntegerField()
    dateofpost=models.DateTimeField(default=datetime.now(),blank=False)
    edited=models.DateTimeField(blank=True,null=True)