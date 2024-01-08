from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Comment


class UserForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "username", "email","phone"]


class EditProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=50,required=False)
    last_name = forms.CharField(max_length=50,required=False)
    username = forms.CharField(max_length=50,required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=15,required=False)

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "username", "email", "phone", "password")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'body')