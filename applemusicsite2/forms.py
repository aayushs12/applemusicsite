from django import forms
from applemusicsite2.models import register
class stform(forms.ModelForm):
    class Meta:
        model=register
        fields=['firstname', 'lastname', 'phn','email','plan','password']
