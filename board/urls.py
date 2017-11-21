from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^new_news/$', views.new_news, name='new_news'),
    url(r'^edit_news/(?P<news_id>\d+)/$', views.edit_news, name='edit_news'),
    url(r'^delete_news/(?P<news_id>\d+)/$', views.delete_news, name='delete_news')
]
