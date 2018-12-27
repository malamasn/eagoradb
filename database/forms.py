from django import forms
from .models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['id' ,'sells']


class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        exclude = ['id']
