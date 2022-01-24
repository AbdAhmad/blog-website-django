from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('post/', user_views.Blog.as_view(), name='post'),
    path('posts/', user_views.Posts.as_view(), name='posts'),
    path('my_posts/', user_views.MyPosts.as_view(), name='my_posts'),
    path('delete_post/<int:pk>/', user_views.DeletePost.as_view(), name='delete_post'),
    path('edit_post/<int:pk>/', user_views.EditPost.as_view(), name='edit_post'),
    path('read_post/<int:pk>/', user_views.ReadPost.as_view(), name='read_post'),
    path('profile/', user_views.ProfilePage.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', user_views.EditProfile.as_view(), name='edit_profile'),
    path('my_post/<int:pk>/', user_views.MyPost.as_view(), name='my_post'),
    path('author/<str:pk>/', user_views.Author.as_view(), name='author'),
    path('author_posts/<str:username>/', user_views.AuthorPosts.as_view(), name="author_posts"),
    path('search/', user_views.Search.as_view(), name="search")
]