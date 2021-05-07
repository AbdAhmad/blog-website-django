from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pic.jpg', upload_to='profile_pictures') 
    location = models.CharField(max_length=100, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)  

    def __str__(self):
        return f"{self.user.username} abcd"