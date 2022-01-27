from django import forms 
from .models import Blog, Profile, Comment
from crispy_forms.helper import FormHelper

class BlogForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_show_labels = False

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title'
            }
        )
    )

    content = forms.CharField( 
        widget=forms.Textarea(
            attrs={
                'rows': 15,
                'placeholder': 'Tell your story...'
            }
        )
    )

    class Meta:
        model = Blog
        fields = ['title', 'content']


class EditProfileForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_show_labels = False

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Full Name'
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email'
            }
        )
    )

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Location'
            }
        )
    )

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'placeholder': 'Bio'
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['full_name', 'email', 'location', 'bio', 'profile_pic']


class CommentForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_show_labels = False

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 3, 
                'placeholder': 'Drop a comment'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ['comment']
