from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Cate)
admin.site.register(announmodel)
admin.site.register(Profile)