from django import forms

class Statement(forms.Form):
    input = forms.CharField(widget=forms.TextInput(attrs={'size':100}), required=True)
