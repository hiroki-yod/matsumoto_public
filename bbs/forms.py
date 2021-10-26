from django import forms
from bbs.models import Bbs, Comment, Like

#投稿
class BbsForm(forms.ModelForm):
    class Meta:
        model = Bbs
        fields = ('description',)

        widgets = {
            'description': forms.Textarea(attrs={'class': 'input-box'})
        }

#コメント
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'input-box'})
        }

#リアクション
class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ()

