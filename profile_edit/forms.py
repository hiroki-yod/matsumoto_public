from django import forms
from profile_edit.models import Profile

#プロフィール設定
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('penname', 'email', 'image',)

#通知設定
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('notice_bbs', 'notice_comment', 'notice_like',)