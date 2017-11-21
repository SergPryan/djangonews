from django import forms

from board.models import News


class NewsForm(forms.ModelForm):
    image = forms.ImageField(label="Есть в наличии")

    class Meta:
        model = News
        fields = '__all__'
