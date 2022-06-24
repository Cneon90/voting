from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
from django.urls import path, include
from django.contrib import admin



urlpatterns = [


    path('', views.home, name='home'),#Главная страница
    path('succeess', views.succeess, name='apply'),  # Главная страница
    path('result', views.result, name='result'),  # Главная страница
    path('chart', views.chart, name='chart'),  # Главная страница
    path('api/count', views.count, name='count'),  # Главная страница
    path('delete/<int:id>', views.delete, name='count'),  # Главная страница
    ]