from django import forms

class Statement(forms.Form):
    input = forms.CharField(required=True)
