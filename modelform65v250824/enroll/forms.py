from django import forms
from django.core import validators
from enroll.models import User

class StudentRegistration(forms.Form):
    first_name = forms.CharField(error_messages={'required':'Enter your firstname'})
    email = forms.EmailField(error_messages={'required':'Enter your email'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your password.'})
    
    
class StudenRegistrationModelForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False) # more priority of max_length to model.py file.
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Name', 'email':'Enter Email', 'password':'Password'}
        help_text = {'name':'Enter Your Full Name'}
        error_messages = {
            'name': {'required':'Naam likhna jaruri hai'}
            }
        widgets = {
            'password': forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'yaha naam likhe'})
            }