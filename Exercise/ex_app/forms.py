from django import forms


class FormAddCompany(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)