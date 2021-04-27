from django import forms
from .models import Registration
from django.forms import ModelForm

class AddWordForm(forms.Form):
    word = forms.CharField(max_length=50)
    translation = forms.CharField(max_length=50)
    
class CheckBoxForm(forms.Form):
    chechbox = forms.BooleanField()

class DeleteWordForm(forms.Form):
    word = forms.CharField(max_length=50)
   

class RegistForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    password_conf = forms.CharField(max_length=50)


class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
