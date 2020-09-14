from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

user = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = user
        #fields = ('__all__')
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
