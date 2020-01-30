from datetime import datetime, date, time, timedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser, GENDER, Tovar, Purchase, Vozvrat


class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Введите e-mail в формате "mylogin@mymail.com"')
    first_name = forms.CharField(max_length=200, label='Имя')
    last_name = forms.CharField(max_length=200, label='Фамилия')
    birthday = forms.DateField(label='Дата рождения', required=False, input_formats=['%d/%m/%Y'])
    gender = forms.CharField(max_length=10, label='Пол', widget=forms.RadioSelect(choices=GENDER), required=False)
    username = forms.CharField(max_length=150, label='Логин')

    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'gender', 'email')
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'date_picker'})
        }


class CreateTovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = '__all__'


class UpdateTovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ('name', 'description', 'price', 'number')


class CreatePurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('article_number', )

