from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import PostForm, EditProfileForm
from .models import Post, Profile
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'blog_app/index.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(password1) < 8:
            messages.error(request, 'Password is too short')
            return redirect('signup')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=first_name, email=email, username=username, password=password1)
                user.save()
                username = request.POST['username']
                password1 = request.POST['password1']
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                messages.success(request, 'Signup was successful')
                return redirect('profile')
        else:
            messages.error(request, "Two passwords didn't match")
            return redirect('signup')

    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'blog_app/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome ' + username)
            return redirect('posts')
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'blog_app/login.html')

@login_required
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

@login_required
def posts(request):

    # fetching latest posts first
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_app/posts.html', {'posts': posts})

@login_required
def my_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-created_at')
    return render(request, 'blog_app/my_posts.html', {'posts': posts})

@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method =="POST":
        post.delete()
        messages.success(request, 'Post deleted succesfully')
        return redirect("my_posts")
    return render(request, 'blog_app/delete.html', {'post': post})

@login_required
def read_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog_app/read_post.html', {'post': post})

@login_required
def my_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog_app/my_post.html', {'post': post})

@login_required
def profile_page(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    posts_count = posts.count()
    profile = Profile.objects.get(user=user)
    return render(request, 'blog_app/profile.html', {'user': user, 'posts_count': posts_count, 'profile': profile})

@login_required
def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        post = PostForm(instance=post)
    else:  # POST
        post = PostForm(request.POST, instance=post)
        if post.is_valid():
            post.save()
            messages.success(request, 'Post updated successfully')
            return redirect('my_posts')
            
    return render(request, 'blog_app/post.html', {'post': post})

@login_required
def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    image_path = profile.image.path
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            if 'default.jpg' in str(image_path):
                form.save()
            # the `form.save` will also update the newest image & path.
            else:
                profile = form.save(commit=False)
                image_posted = form.cleaned_data.get('image')
                try:
                    image_posted_path = getattr(image_posted,'path')
                    if image_path == image_posted_path:
                        profile.save()
                except:
                    if os.path.exists(image_path):
                        os.remove(image_path)
                    profile.save()      
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')

    return render(request, 'blog_app/edit_profile.html', {'profile': profile, 'form': form})

@login_required
def author(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    posts_count = posts.count()
    return render(request, 'blog_app/author.html', {'user': user, 'posts_count': posts_count})

@login_required
def author_posts(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    return render(request, 'blog_app/author_posts.html', {'posts': posts,'user': user})

@login_required
def search(request):
    if request.method == 'POST':
        searched_post = request.POST['search']
        posts = Post.objects.filter(title__icontains=searched_post)
        return render(request, 'blog_app/posts.html', {'posts': posts})