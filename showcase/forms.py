from django import forms
from . import models

class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        exclude = ('slug','models_list')

class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.Phone_model
        exclude = ('slug',)
        