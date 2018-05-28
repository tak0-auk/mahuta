# coding: UTF-8
from django import forms
from .models import Work


class WorkForm(forms.ModelForm):

    summary = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=1024)

    class Meta:
        model = Work
        fields = ('name', 'summary', 'limit_date')


