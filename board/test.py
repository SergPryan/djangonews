from board.models import News

count = 0
for news in range(0, 100):
    count = count + 1
    news = News.objects.create(header='header' + str(count), body='body' + str(count))
    news.save()
