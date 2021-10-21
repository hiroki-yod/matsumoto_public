from django import forms
from bbs.models import Bbs, Comment, Like


class BbsForm(forms.ModelForm):
    class Meta:
        model = Bbs
        fields = ('description',)

        widgets = {
            'description': forms.Textarea(attrs={'class': 'input-box'})
        }
