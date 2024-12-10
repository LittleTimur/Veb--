from django import forms

class ProfileForm(forms.Form):
     name = forms.CharField(initial='Твоё имя', max_length=30, required=False)
     surname = forms.CharField(initial='Твоя фамилия', max_length=30, required=False)
     bio = forms.CharField(max_length=500)
     location = forms.CharField(initial='Напиши город/село/деревню, где ты живёшь', max_length=30, required=False)
     birth_date = forms.DateField(required=False)
     img = forms.ImageField(required=False)