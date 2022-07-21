from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control', }))
    first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control', }))
    first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    
    last_login = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length = 100, widget = forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length = 100, widget = forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_actiave = forms.CharField(max_length = 100, widget = forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',  'last_login', 'is_superuser', 'is_staff', 'is_actiave', 'date_joined')
