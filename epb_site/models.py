from django import forms

class Statement(forms.Form):
    input = forms.CharField(required=True, label='')

class Reset(forms.Form):
    input = "__reset__"
