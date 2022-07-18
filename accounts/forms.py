from cmath import acos
from dataclasses import field
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['firs_name', 'last_name', 'phone_number', 'email', 'password']