from django.conf import settings
from django.core.mail import EmailMessage
from profile_edit.models import Profile
from django.template.loader import render_to_string

#投稿
def main(bbs):
    subject = "【投稿】松本家通信よりお知らせ"
    context = {'bbs':bbs}
    message = render_to_string('bbs/mails/bbs.txt', context)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [settings.DEFAULT_FROM_EMAIL]
    bcc = Profile.objects.filter(notice_bbs=True).values_list('email', flat=True)
    email = EmailMessage(subject, message, from_email, recipient_list, bcc)
    email.send()

#コメント
def comment(bbs, comment, poster):
    subject = "【コメント】松本家通信よりお知らせ"
    context = {'bbs':bbs, 'comment':comment}
    message = render_to_string('bbs/mails/comment.txt', context)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [settings.DEFAULT_FROM_EMAIL]
    if poster.notice_comment:
        bcc = [poster.email]
    else:
        return
    email = EmailMessage(subject, message, from_email, recipient_list, bcc)
    email.send()

#リアクション
def like(bbs, user, poster):
    subject = "【いいね】松本家通信よりお知らせ"
    context = {'bbs':bbs, 'user':user}
    message = render_to_string('bbs/mails/like.txt', context)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [settings.DEFAULT_FROM_EMAIL]
    if poster.notice_like:
        bcc = [poster.email]
    else:
        return
    email = EmailMessage(subject, message, from_email, recipient_list, bcc)
    email.send()
    