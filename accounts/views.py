from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile/new')
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html",{'form': form})
