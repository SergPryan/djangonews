from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from board.forms import NewsForm
from board.models import News


def index(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 20)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'news_list': news}
    return render(request, 'board/index.html', context)


def new_news(request):
    if request.method != "POST":
        form = NewsForm()
    else:
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = form.cleaned_data['image']

            return HttpResponseRedirect(reverse('board:index'))
    context = {'form': form}
    return render(request, 'board/new_news.html', context)


def edit_news(request, news_id):
    news = News.objects.get(id=news_id)
    if request.method != 'POST':
        form = NewsForm(instance=news)
    else:
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('board:index'))
    context = {'form': form, 'news': news}
    return render(request, 'board/edit_news.html', context)


def delete_news(request, news_id):
    News.objects.get(id=news_id).delete()
    return HttpResponseRedirect(reverse('board:index'))
