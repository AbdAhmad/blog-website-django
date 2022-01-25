from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import BlogForm, EditProfileForm, CommentForm
from .models import Blog, Profile, Comment, Like
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required


class Welcome(TemplateView):
    template_name = 'blog_app/index.html'


class CreateBlog(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        post = BlogForm()
        context = {
            'post': post
            }
        return render(request, 'blog_app/post.html', context)

    def post(self, request, *args, **kwargs):
        post = BlogForm(data=request.POST)
        if post.is_valid():
            post = post.save(commit = False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog added successfully')
            return redirect('post')            
        return render(request, 'blog_app/post.html', {'post': post})


class EditPost(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        post = Blog.objects.get(id=kwargs['pk'])
        post = BlogForm(instance=post)
        context = {
            'post': post
            }
        return render(request, 'blog_app/post.html', context)

    def post(self, request, *args, **kwargs):
        post = Blog.objects.get(id=kwargs['pk'])
        post = BlogForm(request.POST, instance=post)
        if post.is_valid():
            post = post.save(commit = False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog updated successfully')
            return redirect('my_posts')            
        return render(request, 'blog_app/post.html', {'post': post})
 

class Posts(LoginRequiredMixin, ListView):

    model = Blog
    context_object_name = 'posts'
    template_name = 'blog_app/posts.html'
    queryset = Blog.objects.all().order_by('-created_at')


class MyPosts(LoginRequiredMixin, ListView):

    model = Blog
    context_object_name = 'posts'
    template_name = 'blog_app/my_posts.html'  
    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user).order_by('-created_at')
 

class DeletePost(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        post = Blog.objects.get(id=kwargs['pk'])
        context = {'post': post}
        return render(request, 'blog_app/delete.html', context)

    def post(self, request, *args, **kwargs):
        post = Blog.objects.get(id=kwargs['pk'])
        post.delete()
        messages.success(request, 'Blog deleted succesfully')
        return redirect("my_posts")


@login_required
def read_post(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog)
    blog.views = blog.views + 1
    likes = Like.objects.filter(blog=blog).count()
    blog.likes = likes
    blog.save()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment added')
        return redirect('read_post', slug=slug)
    comment_form = CommentForm()
    context = {
        'blog': blog,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'blog_app/read_post.html', context)


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
        messages.success(request, 'You have unliked this blog')
    else:
        like = Like(like=True, user=user, blog=blog)
        like.save()
        messages.success(request, 'You have liked this post')
    return redirect('read_post', slug=slug)



class MyPost(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog_app/my_post.html'
    context_object_name = 'post'


class ProfilePage(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        posts = Blog.objects.filter(author=user)
        posts_count = posts.count()
        profile = Profile.objects.get(user=user)
        return render(request, 'blog_app/profile.html', {'user': user, 'posts_count': posts_count, 'profile': profile})


class EditProfile(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['pk'])
        form = EditProfileForm(instance=profile)
        context = {'form': form, 'profile': profile}
        return render(request, 'blog_app/edit_profile.html', context)

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['pk'])
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')            
        return render(request, 'blog_app/edit_profile.html', {'form': form, 'profile': profile})


class Author(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=kwargs['pk'])
        posts = Blog.objects.filter(author=user)
        posts_count = posts.count()
        return render(request, 'blog_app/author.html', {'posts_count': posts_count,'user': user})


class AuthorPosts(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=kwargs['username'])
        posts = Blog.objects.filter(author=user).order_by('-created_at')
        return render(request, 'blog_app/author_posts.html', {'posts': posts,'user': user})
    

class Search(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        searched_post = request.POST['search']
        posts = Blog.objects.filter(title__icontains=searched_post)
        return render(request, 'blog_app/posts.html', {'posts': posts})
