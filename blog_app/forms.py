from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import Post, Profile

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = ['title', 'content']

class EditProfileForm(forms.ModelForm):
 
    class Meta:
        model = Profile
        fields = ['image', 'location', 'bio']
         