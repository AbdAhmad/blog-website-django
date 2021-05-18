from django import forms 
from django.contrib.auth.models import User
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    content = forms.CharField( 
        widget=forms.Textarea(attrs={'placeholder': 'Content'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content']

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'location', 'bio']
         