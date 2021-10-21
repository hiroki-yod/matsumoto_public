from bbs.views import secret
from django.http.response import HttpResponseForbidden
from profile_edit.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from profile_edit.forms import ProfileForm, NoticeForm


@login_required
def profile_new(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = request.user
            profile.save()
            return redirect("/secret")
    else:
        if Profile.objects.filter(username=request.user).exists():
            return redirect('/secret')
        else:
            form = ProfileForm()
    return render(request, "profile_edit/profile_new.html", {'form': form})


@login_required
def profile_edit(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if profile.username != request.user:
        return HttpResponseForbidden("このプロフィールの編集は許可されていません")
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/secret')
    
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_edit/profile_edit.html', {'form': form})


@login_required
def notice(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if profile.username != request.user:
        return HttpResponseForbidden("この通知設定の編集は許可されていません")
    
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/secret')
    
    else:
        form = NoticeForm(instance=profile)
    return render(request, 'profile_edit/notice.html', {'form': form})
