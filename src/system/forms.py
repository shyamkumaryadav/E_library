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
            'date_of_birth': DateInput(),
            'date_of_death': DateInput(),
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
                class="btn btn-{% if object %}success{%else%}primary{%endif%} btn-lg btn-block m-1">''')),
                Column(HTML('''{% if object %}<button type="button"
                class="btn btn-danger btn-lg btn-block m-1"
                data-toggle="modal"
                data-target="#deletemodel">
                Delete
                </button>{%endif%}'''), style='display: none;', id='deletebtn')
                ),
            Row(Column(HTML('''{% if object %}<a style='text-decoration:none;' href={% url 'system:authormanagement' %}><i class="fas fa-arrow-circle-left"></i> Go Back</a>{%endif%}'''),
                       style='display: none;', css_class='btn btn-link', id='goback')),
        )
        self.helper.form_id = 'bookAuthorForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = ''


class BookPublishForm(forms.ModelForm):
    class Meta:
        model = models.BookPublish
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookPublishForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', placeholder="Enter Name"),
            Field('address', placeholder="Enter Address", maxlength=80, rows=2),
            Row(Column(HTML('''<input type="submit" name="{% if object %}update{%else%}add{%endif%}"
                value="{% if object %}Update{%else%}Add{%endif%}"
                class="btn btn-{% if object %}success{%else%}primary{%endif%} btn-lg btn-block m-1">''')
                       ),
                Column(HTML('''{% if object %}<button type="button"
                    class="btn btn-danger btn-lg btn-block m-1"
                    data-toggle="modal"
                    data-target="#deletemodel">
                    Delete
                    </button>{%endif%}'''),
                       style='display: none;text-decoration: none;', id='deletebtn'
                       ),
                ),
            Row(Column(HTML('''{% if object %}<a href={% url 'system:publishermanagement' %}><i class="fas fa-arrow-circle-left"></i> Go Back</a>{%endif%}'''),
                       style='display: none;', css_class='btn btn-link', id='goback')),
        )
        self.helper.form_id = 'bookAuthorForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = ''


class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = '__all__'
        # fields_attrs = {
        # 'publish': {'name': 'Select Publisher'}
        # },
        widgets = {
            'publish_date': DateInput()
            # 'rating': forms.SelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['publish'].empty_label = 'select Publisher'
        self.fields['author'].empty_label = 'select author'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('name', placeholder="Enter Book Name")),
                Column(Field('publish_date'))
            ),
            Row(
                Column(Field('author')),
                Column(Field('publish')),
            ),
            Row(
                Column(Field('language')),
                Column(Field('edition')),
            ),
            Row(
                Column(PrependedAppendedText(
                    'cost', '$', '.00', min=0, step=1),),
                Column(Field('page')),
            ),
            Row(
                Column(Field('description', placeholder='Description',
                             maxlength=100, rows=2))
            ),
            Row(Column(Field('profile'))),
            Row(Column(Field('rating',
                             css_class="custom-range", max=10.0, min=0, attrs={'type': 'range'}))),
            Row(Column(HTML('''<input type="submit" name="{% if object %}update{%else%}{%endif%}"
                value="{% if object %}Update{%else%}Add{%endif%}"
                class="btn btn-{% if object %}success{%else%}primary{%endif%} btn-lg btn-block m-1">''')),
                Column(HTML('''{% if object %}<button type="button"
                class="btn btn-danger btn-lg btn-block m-1"
                data-toggle="modal"
                data-target="#deletemodel">
                Delete
                </button>{%endif%}'''), style='display: none;', id='deletebtn')
                ),
        )
        self.helper.form_id = 'bookForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
