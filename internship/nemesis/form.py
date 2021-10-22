from django import forms
from django.forms import ModelForm
from nemesis.models import *

class userform(forms.ModelForm):
    class Meta:
        model = myuser
        fields = '__all__'