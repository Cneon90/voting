from django import forms

from .models import *
from django.core.exceptions import ValidationError

Select_floor = [
    ('B', 'Мальчик'),
    ('G', 'Девочка')
]


def validate_all_choices(Select_floor):    # here have your custom logic    pass
    pass

class form_voite(forms.Form):

    Name = forms.CharField(label='Имя:', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше имя','size':'20'}))
    floor = forms.ChoiceField(required = False,label='Пол:',choices=Select_floor,widget=forms.NullBooleanSelect(attrs={'class': 'floor',"required": "required"}))

