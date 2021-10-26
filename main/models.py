from django.db import models

#YouTube動画
class Movie(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.CharField('投稿時刻', max_length=128)
    movie_id = models.CharField('ID', max_length=128)

    def __str__(self):
        return self.title

#ニュース（実際の投稿日と表示される投稿日が一致）
class News(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    text = models.TextField('本文')
    image = models.ImageField(verbose_name="ニュース画像", upload_to='images/')
    link_url = models.CharField('URL', blank=True, max_length=128)
    link_text = models.CharField('リンク先', blank=True, max_length=128)

    def __str__(self):
        return self.title

#ニュース（実際の投稿日と表示される投稿日が不一致）
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

#作品（実際の投稿日と表示される投稿日が一致）
class Work(models.Model):
    title = models.CharField('タイトル', max_length=128)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    text = models.TextField('本文')
    image = models.ImageField(verbose_name="ニュース画像", upload_to='images/')
    link_url = models.CharField('URL', max_length=128)
    link_text = models.CharField('リンク先', max_length=128)

    def __str__(self):
        return self.title

#作品（実際の投稿日と表示される投稿日が不一致）
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

#note記事
class Essay(models.Model):
    title = models.CharField('タイトル', blank=True, max_length=128)
    url = models.CharField('URL', max_length=128)
    year = models.IntegerField('Year')
    month = models.IntegerField('Month')
    date = models.IntegerField('Date')

    def __str__(self):
        return self.title