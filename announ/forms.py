from django import forms
from our_models import views
from django.conf import settings

class announForm(forms.Form):
    about = forms.CharField(label="Описание")
    name = forms.CharField(label="Назвние объявления")
    img = forms.ImageField(label="Изображение")
    value = forms.IntegerField(label="Цена за услугу",initial=settings.MEDIA_URL + 'images/default.png', required=False)
    cat = forms.ModelChoiceField(queryset=views.Cat_get_all(), label="Категория")


