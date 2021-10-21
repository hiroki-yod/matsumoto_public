from django.db import models

class Movie(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.CharField('投稿時刻', max_length=128)
    movie_id = models.CharField('ID', max_length=128)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    text = models.TextField('本文')
    image = models.ImageField(verbose_name="ニュース画像", upload_to='images/')
    link_url = models.CharField('URL', blank=True, max_length=128)
    link_text = models.CharField('リンク先', blank=True, max_length=128)

    def __str__(self):
        return self.title


class OldNews(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    text = models.TextField('本文')
    image = models.ImageField(verbose_name="ニュース画像", upload_to='images/')
    link_url = models.CharField('URL', blank=True, max_length=128)
    link_text = models.CharField('リンク先', blank=True, max_length=128)
    year = models.IntegerField('Year')
    month = models.IntegerField('Month')
    date = models.IntegerField('Date')

    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    text = models.TextField('本文')
    image = models.ImageField(verbose_name="ニュース画像", upload_to='images/')
    link_url = models.CharField('URL', max_length=128)
    link_text = models.CharField('リンク先', max_length=128)

    def __str__(self):
        return self.title


class OldWork(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    text = models.TextField('本文')
    image = models.ImageField(verbose_name="ニュース画像", upload_to='images/')
    link_url = models.CharField('URL', blank=True, max_length=128)
    link_text = models.CharField('リンク先', blank=True, max_length=128)
    year = models.IntegerField('Year')
    month = models.IntegerField('Month')
    date = models.IntegerField('Date')

    def __str__(self):
        return self.title


class Essay(models.Model):
    title = models.CharField('タイトル', blank=True, max_length=128)
    url = models.CharField('URL', max_length=128)
    year = models.IntegerField('Year')
    month = models.IntegerField('Month')
    date = models.IntegerField('Date')

    def __str__(self):
        return self.title