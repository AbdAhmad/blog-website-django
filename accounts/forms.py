# from django import forms 
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
# from crispy_forms.helper import FormHelper
# from django.utils.translation import gettext as _

# class SignupForm(UserCreationForm):
    
#     helper = FormHelper()
#     helper.form_show_labels = False

#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Username'
#             }
#         )
#     )

#     password = forms.CharField( 
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder': 'Password'
#             }
#         )
#     )

#     confirm_password = forms.CharField( 
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder': 'Confirm Password'
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ["username", "password", "confirm_password"]

#     error_messages = {
#         'duplicate_username': _("A user with that email already exists."),
#         'password_mismatch': _("The two password fields didn't match."),
#     }  

