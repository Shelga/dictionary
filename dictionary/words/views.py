from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import Dictionary, Registration
from .forms import AddWordForm, CheckBoxForm, DeleteWordForm, RegistForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    get_word = Dictionary.objects.all()
    return render(request, 'words/index.html', {"dictionary": get_word})


def add(request):
    return render(request, 'words/add.html')


def add_word(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = AddWordForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            word = form.cleaned_data.get("word")
            translation = form.cleaned_data.get("translation")
            word_from_form = Dictionary(
                word=word, translation=translation, status=False)
            word_from_form.save()
            return HttpResponseRedirect('index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/add.html')


def delete(request):
    return render(request, 'words/delete.html')


def delete_word(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = DeleteWordForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            word_f = form.cleaned_data.get("word")
            word_from_form = Dictionary(word=word_f)
            Dictionary.objects.filter(word=word_f).delete()
            return HttpResponseRedirect('index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/delete.html')


def register(request):
    return render(request, 'words/registr.html')


def add_new_user(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = RegistForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            name = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            password_conf = form.cleaned_data.get("password_conf")
            reg_from_form = Registration(name=name, password=password, password_conf=password_conf)
            reg_from_form.save()
            return HttpResponseRedirect('index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/registr.html')

def login(request):
    return render(request, 'words/login.html')


def login_user(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = RegistForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            name = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            password_conf = form.cleaned_data.get("password_conf")
            reg_from_form = Registration(name=name, password=password, password_conf=password_conf)
            reg_from_form.save()
            return HttpResponseRedirect('index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/registr.html')