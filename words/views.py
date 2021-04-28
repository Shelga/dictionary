from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import DictionaryLine, User
from .forms import AddWordForm, CheckKnowForm, DeleteWordForm, RegistForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def index(request):
    new_words = DictionaryLine.objects.filter(status=False) 
    return render(request, 'words/index.html', {"dictionary": new_words})


def add(request):
    return render(request, 'words/add.html')


def add_word(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = AddWordForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            word = form.cleaned_data.get("word")
            translation = form.cleaned_data.get("translation")
            word_from_form = DictionaryLine(
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
            word_from_form = DictionaryLine(word=word_f)
            DictionaryLine.objects.filter(word=word_f).delete()
            return HttpResponseRedirect('index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/delete.html')


def register(request):
    return render(request, 'words/registr.html')


def add_person(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = RegistForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            name = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            password_conf = form.cleaned_data.get("password_conf")
            reg_from_form = User(name=name, password=password, password_conf=password_conf)
            reg_from_form.save()
            return HttpResponseRedirect('/index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/registr.html')

def login(request):
    return render(request, 'words/login.html')



def learned_words(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = CheckKnowForm(request.POST)  # A form bound to the POST data
        print(request.POST)
        if form.is_valid():  # All validation rules pass
            know = request.POST['know']
            full_word_know = DictionaryLine.objects.get(word=know)
            full_word_know.status = True
            full_word_know.save()
            return HttpResponseRedirect('/index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/index.html', {"dictionary": get_word})



# auth_user_groups            words_dictionary          
# auth_user_user_permissions  words_registration 

# CREATE TABLE IF NOT EXISTS "words_dictionary" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "word" varchar(50) NOT NULL, "translation" varchar(50) NOT NULL, "status" bool NOT NULL);
# CREATE TABLE IF NOT EXISTS "words_registration" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(50) NOT NULL, "password_conf" varchar(50) NOT NULL, "name" varchar(50) NOT NULL);

