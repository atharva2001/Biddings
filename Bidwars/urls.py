from django.urls import path
from django.conf.urls import url
from Bidwars import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]