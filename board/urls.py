from django.conf.urls import url

from board.controllers import NewsListView
from . import views

urlpatterns = [
    url(r'^$', NewsListView.as_view(template_name='board/index.html'), name='index'),
    url(r'^new_news/$', views.new_news, name='new_news'),
    url(r'^edit_news/(?P<news_id>\d+)/$', views.edit_news, name='edit_news'),
    url(r'^delete_news/(?P<news_id>\d+)/$', views.delete_news, name='delete_news')
]
