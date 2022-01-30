from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog, Profile, Comment, Like
from .forms import BlogForm, EditProfileForm, CommentForm
from .utils import num_formatter


@login_required
def blogs(request):
    searched_blogs = None
    blogs = Blog.objects.all()
    for blog in blogs:
        likes = Like.objects.filter(blog=blog).count()
        blog.likes_count = likes
        blog.formatted_views = num_formatter(blog.views)
        blog.formatted_likes = num_formatter(likes)
        blog.save()
    if request.method == 'POST':
        searched_blogs = request.POST['search']
        blogs = Blog.objects.filter(title__icontains=searched_blogs)
        marked = None
    else:
        if request.GET and ('q' in request.GET) and request.GET['q'] == 'latest':
            blogs = Blog.objects.all().order_by('-created_at')
            marked = 'latest'
        else:
            blogs = Blog.objects.all().order_by('-views')
            marked = 'most_popular'
    context = {
        'blogs': blogs,
        'marked': marked,
        'page_title': 'Blogs',
        'searched_blogs': searched_blogs
    }
    return render(request, 'blog_app/blogs.html', context)


@login_required
def create_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(data=request.POST)
        if blog_form.is_valid():
            blog = blog_form.save(commit = False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Blog created successfully')
            return redirect('read_blog', slug=blog.slug)            
    else:
        blog_form = BlogForm()
        context = {
            'blog_form': blog_form
            }
    return render(request, 'blog_app/write_blog.html', context)


@login_required
def read_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog)
    blog.views = blog.views + 1
    likes_count = Like.objects.filter(blog=blog).count()
    blog.likes_count = likes_count
    blog.save()
    is_authorized = False
    liked = False
    try:
        blog_likes = Like.objects.filter(blog=blog)
        like = blog_likes.get(user=request.user)
    except Like.DoesNotExist:
        like = None
    if like is not None:
        liked = True
    if blog.author == request.user:
        is_authorized = True
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment added')
        return redirect('read_blog', slug=blog.slug)
    comment_form = CommentForm()
    context = {
        'blog': blog,
        'comment_form': comment_form,
        'comments': comments,
        'is_authorized': is_authorized,
        'liked': liked
    }
    return render(request, 'blog_app/read_blog.html', context)


@login_required
def update_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=blog)
        if blog_form.is_valid():
            blog = blog_form.save(commit = False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Blog updated successfully')
            return redirect('my_blog', slug=blog.slug) 

    blog_form = BlogForm(instance=blog)
    context = {
        'blog_form': blog_form
    }
    return render(request, 'blog_app/write_blog.html', context)


@login_required
def my_blogs(request):
    if request.GET and ('q' in request.GET) and request.GET['q'] == 'latest':
        blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
        marked = 'latest'
    else:
        blogs = Blog.objects.filter(author=request.user).order_by('-views')
        marked = 'most_popular'
    
    context = {
        'blogs': blogs,
        'marked': marked,
        'page_title': 'My Blogs'
    }
    return render(request, 'blog_app/blogs.html', context)


@login_required
def author_blogs(request, username):
    user = User.objects.get(username=username)
    if request.GET and ('q' in request.GET) and request.GET['q'] == 'latest':
        blogs = Blog.objects.filter(author=user).order_by('-created_at')
        marked = 'latest'
    else:
        blogs = Blog.objects.filter(author=user).order_by('-views')
        marked = 'mostviewed'
    context = {
        'blogs': blogs,
        'marked': marked,
        'page_title': 'Author Blogs'
    }
    return render(request, 'blog_app/blogs.html', context)

 
@login_required
def delete_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    messages.success(request, 'Blog Deleted')
    return redirect('my_blogs')


@login_required
def my_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog)
    blog.views = blog.views + 1
    likes_count = Like.objects.filter(blog=blog).count()
    blog.likes_count = likes_count
    blog.save()
    is_authorized = False
    if blog.author == request.user:
        is_authorized = True
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment added')
        return redirect('read_blog', slug=blog.slug)
    comment_form = CommentForm()
    context = {
        'blog': blog,
        'comment_form': comment_form,
        'comments': comments,
        'is_authorized': is_authorized
    }
    return render(request, 'blog_app/read_blog.html', context)


@login_required
def update_profile(request, pk):
    if request.method == 'POST':
        profile = Profile.objects.get(id=pk)
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('author', username=request.user)            
    else:
        profile = Profile.objects.get(id=pk)
        form = EditProfileForm(instance=profile)
    context = {
        'form': form, 
        'profile': profile
        }
    return render(request, 'blog_app/update_profile.html', context)


@login_required
def author(request, username):
    is_authorized = False
    user = User.objects.get(username=username)
    if str(user.username) == str(request.user):
        is_authorized = True
    profile = Profile.objects.get(user=user)
    posts = Blog.objects.filter(author=user)
    posts_count = posts.count()
    context = {
        'profile': profile,
        'posts_count': posts_count,
        'user': user,
        'is_authorized': is_authorized
    }
    return render(request, 'blog_app/author.html', context)


@login_required
def like_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    user = request.user
    try:
        user_likes = Like.objects.filter(user=user)
        like = user_likes.get(blog=blog)
    except Like.DoesNotExist:
        like = None

    if like is not None:
        like.delete()
        messages.info(request, 'You have unliked this blog')
    else:
        like = Like(like=True, user=user, blog=blog)
        like.save()
        blog.user_likes.add(like)
        blog.save()
        messages.success(request, 'You have liked this post')

    if 'blogs' in request.META.get('HTTP_REFERER'):
        return redirect('blogs')
    elif 'read_blog' in request.META.get('HTTP_REFERER'):
        return redirect('read_blog', slug=slug)

    