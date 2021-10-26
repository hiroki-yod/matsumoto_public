from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

#知らない人から登録されないように本番環境でのみアクセス制限を有効化
#@login_required
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile/new')
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html",{'form': form})
