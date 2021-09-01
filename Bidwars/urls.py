from django.urls import path
from django.conf.urls import url
from Bidwars import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
]