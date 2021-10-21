from django.db import models
from django.conf import settings


class Profile(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="ID", on_delete=models.CASCADE)
    penname = models.CharField('名前', max_length=128)
    email = models.CharField('メールアドレス', max_length=128)
    image = models.ImageField(verbose_name="プロフィール画像", upload_to='images/')
    notice_bbs = models.BooleanField('投稿通知', default=False)
    notice_comment = models.BooleanField('コメント通知', default=False)
    notice_like = models.BooleanField('いいね通知', default=False)
    

    def __str__(self):
        return self.penname
