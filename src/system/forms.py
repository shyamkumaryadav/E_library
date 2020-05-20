from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *


class ExampleForm(forms.Form):
    name = forms.CharField()
