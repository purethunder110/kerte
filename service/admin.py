from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import *
# Register your models here.

class ProjectAdmin(GuardedModelAdmin):
    pass

admin.site.register(Base_user)