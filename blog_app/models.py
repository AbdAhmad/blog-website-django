from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    slug = AutoSlugField(populate_from='title', always_update=True)
    views = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    formatted_views = models.CharField(max_length=10, default='')
    formatted_likes = models.CharField(max_length=10, default='')
    user_likes = models.ManyToManyField('blog_app.Like', blank=True, related_name='user_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:50]


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50]


class Like(models.Model):
    like = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='N/A')
    email = models.EmailField(max_length=254, default='N/A')
    location = models.CharField(max_length=100, default='N/A')
    bio = models.TextField(default='N/A')
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.png')
    blogs = models.ManyToManyField(Blog, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username