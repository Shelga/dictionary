
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index),
    path('add', views.add, name="add"),
    path('add_word', views.add_word),
    path('delete', views.delete),
    path('delete_word', views.delete_word),
    path('register', views.register),
     path('add_person', views.add_person),
]