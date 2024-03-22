
from django import forms
from .models import *
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
                    "first_name":forms.TextInput(attrs={"class": "form-control mb-1","type":"text","placeholder":'First name'}),
                    "last_name":forms.TextInput(attrs={"class": "form-control mb-1","type":"text","placeholder":'Last name'}),
                    "phone":forms.NumberInput(attrs={"class": "form-control mb-1","type":"tel","placeholder":'Primary Phone number' }),
                    "phone2":forms.NumberInput(attrs={"class": "form-control mb-1","type":"tel","placeholder":'Secondary Phone number' }),
                    "email":forms.EmailInput(attrs={"class": "form-control mb-1","type":"text" ,"placeholder":'Your email'}),
                    "field_of_interest":forms.Select(attrs={"class": "form-select mb-1" }),
                    
                 }

