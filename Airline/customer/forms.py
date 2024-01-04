from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class UserForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "username", "email","phone"]
        first_name = forms.CharField(initial = "1234")
