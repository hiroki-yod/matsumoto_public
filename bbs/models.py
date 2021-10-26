from profile_edit.models import Profile
from django.db import models

#投稿
class Bbs(models.Model):
    description = models.TextField('投稿', blank=True)
    created_by = models.ForeignKey(Profile, verbose_name="投稿者", on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)

    def __str__(self):
        return self.description
        
#コメント
class Comment(models.Model):
    text = models.TextField("コメント", blank=False)
    commented_by = models.ForeignKey(Profile, verbose_name="投稿者", on_delete=models.CASCADE)
    commented_to = models.ForeignKey(Bbs, verbose_name="投稿", on_delete=models.CASCADE)
    commented_at = models.DateTimeField("投稿日", auto_now_add=True)

#リアクション
class Like(models.Model):
    liked_to = models.ForeignKey(Bbs, verbose_name="投稿", on_delete=models.CASCADE)
    liked_by = models.ForeignKey(Profile, verbose_name="賛同者", on_delete=models.CASCADE)
    liked_at = models.DateTimeField("賛同日", auto_now_add=True)
