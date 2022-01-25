from logging import PlaceHolder
from xml.etree.ElementTree import Comment
from django import forms 
from .models import Blog, Profile, Comment
from crispy_forms.helper import FormHelper

class BlogForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    content = forms.CharField( 
        widget=forms.Textarea(attrs={'placeholder': 'Content'})
    )

    class Meta:
        model = Blog
        fields = ['title', 'content']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['location', 'bio', 'full_name', 'email']


class CommentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Drop a comment'}))

    class Meta:
        model = Comment
        fields = ['comment']


         