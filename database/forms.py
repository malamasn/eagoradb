from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=45, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=30, required=False, help_text='Optional.')
    city = forms.CharField(max_length=30, required=False, help_text='Optional.')
    phone = forms.IntegerField(min_value=1000000000, max_value=9999999999, required=False, help_text='Optional.')
    credit_card = forms.IntegerField(min_value=1000000000000000, max_value=9999999999999999,
                                    required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                    'address', 'city', 'credit_card', 'phone')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['id' ,'sells']


class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        exclude = ['id']
