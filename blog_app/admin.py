from django.contrib import admin
from .models import Blog, Profile, Comment, Like
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Like)