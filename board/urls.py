from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^new_news/', views.new_news, name='new_news')
]
