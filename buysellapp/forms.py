import re
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"))
    username = forms.RegexField(regex=r'^\d{10}$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Contact"), error_messages={ 'invalid': ("Enter a 10 digit number") })
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("RollNo"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("This Contact already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
