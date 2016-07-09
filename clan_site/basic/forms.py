from django import forms
from django.contrib.admin.widgets import AdminDateWidget 
from django.forms import ModelForm
from basic.models import *
from battles.models import *
from itertools import chain

class RulesForm(forms.Form):
    rule_content = forms.CharField(label='Rule', widget=forms.Textarea, max_length=1000)
