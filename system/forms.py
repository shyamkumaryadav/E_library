from django import forms
from . import models



class UserLoginForm(forms.ModelForm):
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete': 'Password', 'placeholder' : 'Enter Password'}),
    )

    class Meta:
        model = models.Member
        fields = ("username","state")
