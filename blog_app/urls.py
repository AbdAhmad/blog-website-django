from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='welcome'),
    path('write_blog/', views.create_blog, name='write_blog'),
    path('blogs/', views.blogs, name='blogs'),
    path('like_blog/<str:slug>', views.like_blog, name='like_blog'),
    path('my_blogs/', views.my_blogs, name='my_blogs'),
    path('delete_blog/<str:slug>/', views.delete_blog, name='delete_blog'),
    path('update_blog/<str:slug>/', views.update_blog, name='update_blog'),
    path('read_blog/<str:slug>/', views.read_blog, name='read_blog'),
    path('update_profile/<int:pk>/', views.update_profile, name='update_profile'),
    path('my_blog/<str:slug>/', views.my_blog, name='my_blog'),
    path('author/<str:username>/', views.author, name='author'),
    path('author_blogs/<str:username>/', views.author_blogs, name="author_posts")
]
