from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddParkSpace(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].empty_label = "Машина не выбрана"
        self.fields['car'].queryset = Car.objects.filter(parking_space__exact=None)
        self.fields['car'].label = 'Машина'
        self.fields['number'].label = 'Номер'
        self.fields['price'].label = 'Цена'
        self.fields['is_occupied'].label = 'Пометить как занятое'
        self.fields['is_occupied'].required = False

    class Meta:
        model = ParkingSpace
        fields = '__all__'

    def clean_number(self):
        num = self.cleaned_data['number']
        if num > 999 or num < 1:
            raise ValidationError('Номер парковочного места должен быть в диапазоне от 1 до 999')
        return num

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена должна быть положительной')
        return price


class UpdatePrice(forms.Form):
    price = forms.IntegerField(label='Цена')

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена должна быть положительной')
        return price
