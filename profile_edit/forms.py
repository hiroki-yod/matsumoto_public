from django import forms
from profile_edit.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('penname', 'email', 'image',)

        
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('notice_bbs', 'notice_comment', 'notice_like',)