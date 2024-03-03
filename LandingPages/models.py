from django.db import models
from django.contrib.auth import get_user_model
import uuid
#from datetime import datetime
from django.utils import timezone
# Create your models here.

class Community(models.Model):
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Owner=models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING)
    name=models.CharField()
    restricted=models.BooleanField(default=False)
    description=models.TextField()
    
    def get_uuid(self):
        return self.uuid

class tags(models.Model):
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Community=models.ForeignKey(Community,on_delete=models.DO_NOTHING)
    name=models.CharField(10)
    description=models.TextField()

class NewPost(models.Model):
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    User=models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=100)
    post_score=models.IntegerField(blank=True,null=True)
    Community=models.ForeignKey(Community,on_delete=models.DO_NOTHING,blank=True,null=True)
    tags=models.ForeignKey(tags,on_delete=models.DO_NOTHING,blank=True,null=True)
    restricted=models.BooleanField(default=False)
    archived=models.BooleanField(default=True)
    body=models.TextField()
    Upvote=models.IntegerField()
    Downvote=models.IntegerField()
    dateofpost=models.DateTimeField(default=timezone.now,blank=False)
    edited=models.DateTimeField(blank=True,null=True)

    def get_postid(self):
        return self.uuid
    
    def get_userofpost(self):
        return self.User.username

class community_user_group(models.Model):
    community=models.ForeignKey(Community,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING)
    designation=models.CharField(10)