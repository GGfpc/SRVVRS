from django import forms
from django.contrib.auth import authenticate, login, logout

class LogIn(forms.Form):
    user = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        user = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if user and password:
            user = authenticate(username=user,password=password)

            if not user or password:
                raise forms.ValidationError("As credenciais estão incorrectas")

        return super(LogIn,self).clean(*args, **kwargs)
