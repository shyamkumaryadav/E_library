from django import forms
from . import models
from account.forms import DateInput
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *


class BookAuthorForm(forms.ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = '__all__'
        widgets = {
            'date_of_birth' : DateInput(),
            'date_of_death' : DateInput(),
        }
    def __init__(self, *args, **kwargs):
        super(BookAuthorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('first_name', placeholder="Enter First Name")),
                Column(Field('last_name', placeholder="Enter Last Name")),
            ),
            Row(
                Column(Field('date_of_birth')),
                Column(Field('date_of_death')),
            ),
            Row(Column(HTML('''<input type="submit" name="{% if object %}update{%else%}add{%endif%}"
                value="{% if object %}Update{%else%}Add{%endif%}"
                class="btn btn-primary btn-lg btn-block m-1" 
                style="text-shadow: 3px 6px 6px black;">''')),
                Column(HTML('''{% if object %}<button type="submit" name="Delete"
                value="{{ object.id }}"
                class="btn btn-danger btn-lg btn-block m-1" 
                style="text-shadow: 3px 6px 6px black;">Delete</button>{%endif%}'''))
            ),
        )
        self.helper.form_id = 'bookAuthorForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = ''


class ExampleForm(forms.Form):
    name = forms.CharField()
