
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index),
    path('add', views.add, name="add"),
    path('add_word', views.add_word),
    path('delete', views.delete),
    path('api/word/delete', views.delete_word),
    path('register', views.register),
    path('add_person', views.add_person),
    path('login', views.login),
    path('api/word/learn', views.learned_words),
    # path('api/word/forget', views.words_forgotten),
    # path('forgotten', views.words_forgotten),
]

