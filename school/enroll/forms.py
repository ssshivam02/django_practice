from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    first_name = forms.CharField(error_messages={'required':'Enter your firstname'})
    email = forms.EmailField(error_messages={'required':'Enter your email'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your password.'})
    