
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, DateTimeInput
from django.core.exceptions import ValidationError
from django import forms

from . models import Task

# register a user 

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2',]

# --login user        


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#-- create a task

class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Task
        fields = ['title','content', 'due_date',]
        widgets = {
            'due_date': forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'yyyy-mm-dd'}),

        }


class UpdateUserForm(forms.ModelForm):
    
    password = None

    class Meta:

        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]
