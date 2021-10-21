from django.contrib import admin
from bbs.models import Bbs, Comment, Like
from profile_edit.models import Profile


admin.site.register(Bbs)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
