from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(NewPost)
admin.site.register(Community)