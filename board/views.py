from django.shortcuts import render

from board.models import News


def index(request):
    news_list = News.objects.all()
    context = {'news_list': news_list}
    return render(request, 'board/index.html', context)
