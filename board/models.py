from django.db import models


class NewsManager(models.Manager):
    def create_book(self, header, body):
        news = self.create(header=header, body=body)
        return news


class News(models.Model):
    header = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/thumbnails/%Y/%m/%d')

    class Meta:
        db_table = 'news'
