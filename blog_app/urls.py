from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.CreateBlog.as_view(), name='post'),
    path('posts/', views.Posts.as_view(), name='posts'),
    path('my_posts/', views.MyPosts.as_view(), name='my_posts'),
    path('delete_post/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),
    path('edit_post/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path('read_post/<str:slug>/', views.ReadPost.as_view(), name='read_post'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', views.EditProfile.as_view(), name='edit_profile'),
    path('my_post/<str:slug>/', views.MyPost.as_view(), name='my_post'),
    path('author/<str:pk>/', views.Author.as_view(), name='author'),
    path('author_posts/<str:username>/', views.AuthorPosts.as_view(), name="author_posts"),
    path('search/', views.Search.as_view(), name="search")
]