from django import forms

class AddWordForm(forms.Form):
    word = forms.CharField(max_length=50)
    translation = forms.CharField(max_length=50)
    
class CheckBoxForm(forms.Form):
    chechbox = forms.BooleanField()

class DeleteWordForm(forms.Form):
    word = forms.CharField(max_length=50)
   

class RegistForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    password_conf = forms.CharField(max_length=50)