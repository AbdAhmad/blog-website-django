from django import forms 
from django.contrib.auth.models import User
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']

class EditProfileForm(forms.ModelForm):
 
    class Meta:
        model = Profile
        fields = ['image', 'location', 'bio']
         