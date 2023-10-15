from django.forms import ModelForm
from .models import User

class User_Signup_form(ModelForm):
    """
    This is a form that creates a user in database
    used to sign up a user on website
    it will take username, email, password,first name, last name, phone number
    """
    class Meta:
        model = User
        fields = ["username", "email","password","phone_number","first_name","last_name"]



class User_Signin_form(ModelForm):
    """
    This is a form that takes data from user and validates that
    used to sign in a existing user on website
    it will take username, password
    """
    class Meta:
        model = User
        fields = ["username","password"]

from django import forms


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number']