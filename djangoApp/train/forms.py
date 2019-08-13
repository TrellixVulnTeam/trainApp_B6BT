from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Class meta
    # model that will be affected is user model
    # Fields below are the fields we want in the form and in that order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']