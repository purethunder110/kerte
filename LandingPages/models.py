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
    
    def __str__(self) -> str:
        return f"{self.name}:{self.uuid}"

class tags(models.Model):
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Community=models.ForeignKey(Community,on_delete=models.DO_NOTHING)
    name=models.CharField(10)
    description=models.TextField()

    def __str__(self):
        return f"{self.Community.name}:{self.name}"

class NewPost(models.Model):
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    User=models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    #post_score=models.IntegerField(blank=True,null=True)
    Community=models.ForeignKey(Community,on_delete=models.DO_NOTHING,blank=True,null=True)
    tags=models.ForeignKey(tags,on_delete=models.DO_NOTHING,blank=True,null=True)
    restricted=models.BooleanField(default=False)
    archived=models.BooleanField(default=False)
    body=models.TextField()
    banner=models.ImageField(default="static/images/Default_Banner.jpg",upload_to="static/UserGenerated/Post_Banner/Post_Banner")
    #Upvote=models.IntegerField()
    #Downvote=models.IntegerField()
    dateofpost=models.DateTimeField(default=timezone.now,blank=False)
    edited=models.DateTimeField(blank=True,null=True)

    def get_postid(self):
        return self.uuid
    
    def get_userofpost(self):
        return self.User.username
    
    def __str__(self):
        return f"{self.Community.name}-|-{self.title}"

class community_user_group(models.Model):
    community=models.ForeignKey(Community,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING)
    designation=models.CharField(10)