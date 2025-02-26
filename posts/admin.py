from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)
# Compare this snippet from posts/models.py:
#
# from django.db import models  
# from django.contrib.auth.models import User
