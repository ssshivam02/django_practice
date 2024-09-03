from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms 

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(max_length=100, label='Confirm Password',widget=forms.PasswordInput, required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        lables = {'email':'Email'}
        
class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        lables = {'email':'Email'}
        