# coding: UTF-8
from django import forms
from .models import Work


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('name', 'summary', 'limit_date')


