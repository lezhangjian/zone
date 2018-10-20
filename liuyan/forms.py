# -*- coding:utf-8 -*-
from django import forms


class LiuyanForm(forms.Form):
    name = forms.CharField(required=True, label='Your name', max_length=20, min_length=3)
    message = forms.CharField(max_length=120, label='message')