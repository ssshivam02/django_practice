from django import forms
from enroll.models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','password','email']
        widgets = {'password':forms.PasswordInput}