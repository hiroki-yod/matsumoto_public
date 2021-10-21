from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Count
from bbs.models import Bbs, Comment, Like
from bbs.forms import BbsForm, CommentForm
from bbs.modules import notification
from profile_edit.models import Profile

import environ
env = environ.Env()
env.read_env('.env')


@login_required
def secret(request):
    if request.method == 'POST':
        form = BbsForm(request.POST)
        if form.is_valid():
            bbs = form.save(commit=False)
            bbs.created_by = Profile.objects.get(username=request.user)
            bbs.save()
            notification.main(bbs)
        return redirect("/secret")
    else:
        form = BbsForm()
    bbss = Bbs.objects.annotate(comment_cnt=Count('comment')).annotate(like_cnt=Count('like')).order_by('created_at').reverse()
    user_profile = Profile.objects.get(username=request.user)
    drive_url = env("GOOGLE_DRIVE_URL")
    calendar_url = env("GOOGLE_CALENDAR_URL")
    context = {"bbss": bbss, "user_profile":user_profile, 'form':form, "drive_url": drive_url, "calendar_url": calendar_url}
    return render(request, "bbs/secret.html", context)


@login_required
def post_detail(request, post_id):
    if request.method == 'POST':
        if "button_1" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.commented_by = Profile.objects.get(username=request.user)
                comment.commented_to = Bbs.objects.get(id=post_id)
                comment.save()
                bbs = Bbs.objects.get(id=post_id)
                poster = bbs.created_by
                notification.comment(bbs, comment, poster)
            return redirect('bbs:post_detail', post_id=post_id)
        elif "button_2" in request.POST:
            user = Profile.objects.get(username=request.user)
            article = Bbs.objects.get(id=post_id)
            like = Like.objects.filter(liked_by=user, liked_to=article)
            if like.exists():
                like.delete()
            else:
                Like.objects.create(liked_by=user, liked_to=article)
                bbs = Bbs.objects.get(id=post_id)
                like = Like.objects.filter(liked_to__id=post_id)
                poster = bbs.created_by
                notification.like(bbs, user, poster)
            return redirect('bbs:post_detail', post_id=post_id)
        else:
            return redirect('bbs:post_detail', post_id=post_id)
    else:
        form = CommentForm()
    bbs = Bbs.objects.get(id=post_id)
    likes = Like.objects.filter(liked_to__id=post_id)
    comments = Comment.objects.filter(commented_to__id = post_id)
    user_profile = Profile.objects.get(username=request.user)
    drive_url = env("GOOGLE_DRIVE_URL")
    context = {"bbs": bbs, "comments": comments, "user_profile":user_profile, 'form':form, 'likes':likes, "drive_url": drive_url}
    return render(request, "bbs/post_detail.html", context)

