
from django.urls import path
from . import views
from django.urls import include
# from django.contrib.auth import views


urlpatterns = [
    path('index', views.index),
    path('add', views.add, name="add"),
    path('add_word', views.add_word),
    path('delete', views.delete),
    path('delete_word', views.delete_word),
    path('register', views.register),
    path('add_new_user', views.add_new_user),
     path('login', views.login),
    # path('login_user', views.login_user),
    path('learned_words', views.learned_words),
    path('words_forgotten', views.words_forgotten),
    path('forgotten', views.forgotten),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sorry', views.sorry),
   
]

