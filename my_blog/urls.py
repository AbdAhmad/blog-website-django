"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from blog_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from blog_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index, name='index'),
    path('signup/', user_views.signup, name="signup"),
    path('login/', user_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog_app/logout.html'), name='logout'),
    path('post/', user_views.post, name='post'),
    path('posts/', user_views.posts, name='posts'),
    path('my_posts/', user_views.my_posts, name='my_posts'),
    path('delete_post/<int:id>/', user_views.delete_post, name='delete_post'),
    path('edit_post/<int:id>/', user_views.edit_post, name='edit_post'),
    path('read_post/<int:id>/', user_views.read_post, name='read_post'),
    path('profile/', user_views.profile_page, name='profile'),
    path('edit_profile/<int:id>/', user_views.edit_profile, name='edit_profile'),
    path('my_post/<int:id>/', user_views.my_post, name='my_post'),
    path('author/<str:username>/', user_views.author, name='author'),
    path('author_posts/<str:username>', user_views.author_posts, name="author_posts"),
    path('search', user_views.search, name="search")
]

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
