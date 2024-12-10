from django import forms
from django.forms import ModelForm
from our_models.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'surname', 'subject', 'body', 'sender']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})