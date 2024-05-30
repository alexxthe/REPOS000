#from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import SummitTalk, LeaderTalk

admin.site.register(SummitTalk)
admin.site.register(LeaderTalk)
