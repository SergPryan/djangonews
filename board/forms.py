from django import forms

from board.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
