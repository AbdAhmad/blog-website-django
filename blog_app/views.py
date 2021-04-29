from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, PostForm, EditProfileForm
from .models import Post, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign up successfully')
            return redirect('post')

    else:
        form = SignupForm()
    return render(request, 'blog_app/signup.html', {'form': form})


def post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit = False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post added successfully')
            return redirect('post')
    else:
        post = PostForm()
    return render(request, 'blog_app/post.html', {'post': post})

def posts(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'blog_app/posts.html', {'posts': posts})

def myposts(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    return render(request, 'blog_app/myposts.html', {'posts': posts})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method =="POST":
        post.delete()
        messages.success(request, 'Post deleted succesfully')
        return redirect("myposts")
    return render(request, 'blog_app/delete.html', {'post': post})

def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        post = PostForm(instance=post)
    else:  # POST
        post = PostForm(request.POST, instance=post)
        if post.is_valid():
            post.save()
            messages.success(request, 'Post updated successfully')
            return redirect('myposts')
            
    return render(request, 'blog_app/post.html', {'post': post})

def read_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog_app/read_post.html', {'post': post})

@login_required
def profile_page(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    posts_count = posts.count()
    profile = Profile.objects.get(user=user)
    return render(request, 'blog_app/profile.html', {'user': user, 'posts_count': posts_count, 'profile': profile})

def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            # deleting old uploaded image.
            image_path = profile.image.path
            if os.path.exists(image_path):
                os.remove(image_path)

            # the `form.save` will also update the newest image & path.
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
    return render(request, 'blog_app/edit_profile.html', {'profile': profile, 'form': form})
