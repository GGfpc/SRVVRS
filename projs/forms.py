from django import forms


class LogIn(forms.Form):
    user = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())


