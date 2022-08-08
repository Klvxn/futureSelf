# from ckeditor.widgets import CKEditorWidget
from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Letter
from .tasks import send_email

# Forms
class LetterForm(forms.ModelForm):
    
    message = forms.CharField(
        required=True,
        label='Your Letter',
        initial='Dear futureSelf,\n',
        widget=forms.Textarea(attrs={'':''})
    )
    date = forms.DateField(
        label='Date to deliver',
        required=True, 
        help_text='Date should be a month from now.',
        widget=forms.DateInput(attrs={'type':'date', 'id':'date'})
    )
    email_address = forms.EmailField(
        label='Your Email address',
        required=True,
        widget=forms.EmailInput(attrs={
            'type':'email',
            'id':'email',
            'placeholder':'Enter a valid email address'
        })
    )

    class Meta:
        model = Letter
        exclude = ('id', 'user', 'delivered')
       
    def clean_message(self):
        message = self.cleaned_data['message']
        if not message or message == ' ':
            raise forms.ValidationError(r'Can\'t send empty message.')
        return message

    def clean_date(self):
        date = self.cleaned_data['date']
        now = timezone.now().date()
        if date - now < timedelta(days=28):
            raise forms.ValidationError('Date is too early.')
        return date
