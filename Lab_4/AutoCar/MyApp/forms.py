from django import forms
from .models import *


class AddParkSpace(forms.Form):
    number = forms.IntegerField()
    price = forms.IntegerField()
    is_occupied = forms.BooleanField()
    Car = forms.ModelChoiceField(queryset=Car.objects.filter())
