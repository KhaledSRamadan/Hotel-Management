from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	
    class Meta(UserCreationForm):
        model = CustomUser
        img=forms.ImageField()
        fields= ('username','email','first_name','last_name','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        img=forms.ImageField()

        fields = ('username', 'email','type','userage','userphone','usercreditcard','creditcard_cvv','creditcard_ED','img')