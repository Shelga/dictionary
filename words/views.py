from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import DictionaryLine, New_user
from .forms import AddWordForm, CheckKnowForm, DeleteWordForm, RegistForm
from django.contrib.auth.forms import UserCreationForm

from random import choice
from string import ascii_letters
# Create your views here.



def index(request):
    new_words = DictionaryLine.objects.filter(status=False) 

    numvisit=DictionaryLine.objects.count()  # The 'all()' is implied by default.
    print(request.META)
    # print(request.headers)

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'words/index.html', {"dictionary": new_words,  'num_visits': num_visits})
    

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
        # bearer_token_header = request.META["Authorization"][7:]
        # current_user = New_user.objects.filter(bearer_token=bearer_token_header)
        current_user = New_user.objects.filter(name=USER)
        if current_user is None:
            return render(request, 'words/login.html')
        else:
            form = DeleteWordForm(request.POST)  # A form bound to the POST data
            if form.is_valid():  # All validation rules pass
                word_f = form.cleaned_data.get("word")
                word_from_form = DictionaryLine(word=word_f)
                DictionaryLine.objects.filter(word=word_f).delete()
                return HttpResponseRedirect('index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/delete.html')


def register(request):
    return render(request, 'words/register.html')


def add_new_user(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = RegistForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            name = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            password_conf = form.cleaned_data.get("password_conf")
            reg_from_form = New_user(name=name, password=password, password_conf=password_conf)
            reg_from_form.save()
            return HttpResponseRedirect('index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/register.html')

def login(request):
    return render(request, 'words/login.html')

def sorry(request):
    return render(request, 'words/sorry.html')

def login_user(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = RegistForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            name_login = form.cleaned_data.get("name")
            password_login = form.cleaned_data.get("password")
            # bearer_token = ''.join(choice(ascii_letters) for i in range(12))
            if New_user.objects.filter(name=name_login, password=password_login):
                # if 
                return HttpResponseRedirect('index')  # Redirect after POST
            else:
                return HttpResponseRedirect('sorry')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/register.html')


def learned_words(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = CheckKnowForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            know = request.POST['know']
            full_word_know = DictionaryLine.objects.get(word=know)
            full_word_know.status = True
            full_word_know.save()
            return HttpResponseRedirect('/index')  # Redirect after POST
    if request.method == 'GET':
        return render(request, 'words/index.html', {"dictionary": get_word})


def forgotten(request):
    return render(request, 'words/forgotten.html')


def words_forgotten(request):
    new_words_forgotten = DictionaryLine.objects.filter(status=True) 
    return render(request, 'words/forgotten.html', {"dictionary": new_words_forgotten})
    
