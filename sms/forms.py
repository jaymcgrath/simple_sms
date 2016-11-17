from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(label='Your message (max 140 chars)', max_length=140)
    number = forms.CharField(label='Number of recipient, no hyphens', max_length=12, initial="+1")

    class Meta:
        fields = ['message', 'number']
