from django.urls import path
from django.conf.urls import url
from Biddings import views
from django.contrib import admin

urlpatterns = [
    path('https://biddings1.herokuapp.com', views.index, name='index'),
]