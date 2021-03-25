from django import forms
from . import models
from account.forms import DateInput
from django.utils import timezone
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from account.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _


def get_today(now=timezone.now()):
    date = timezone.datetime(now.year - 15, now.month,
                             now.day).date().__str__()
    return date


class BookAuthorForm(forms.ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
            'date_of_death': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(BookAuthorForm, self).__init__(*args, **kwargs)
        self.auto_id = "%s"
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('first_name', placeholder="Enter First Name")),
                Column(Field(
                    'last_name', placeholder="Enter Last Name")),
            ),
            Row(
                Column(Field('date_of_birth')),
                Column(Field('date_of_death')),
            ),
            Row(Column(Submit('submit', str('Update' if self.initial else 'Add'), css_class=f'btn btn-{"success" if self.initial else "primary"} btn-lg btn-block m-1')),
                Column(HTML('''{% if object %}<button type="button"
                    class="btn btn-danger btn-lg btn-block m-1"
                    data-toggle="modal"
                    data-target="#deletemodel">
                    Delete
                    </button>{% endif %}'''),
                       id='deletebtn'
                       ) if self.initial else None,
                ),
            Row(Column(HTML('''{% if object %}<a style='text-decoration:none;' href={% url 'system:authormanagement' %}><i class="fas fa-arrow-circle-left"></i> Go Back</a>{%endif%}'''),
                       css_class='btn btn-link')),
        )
        self.helper.form_id = 'bookAuthorForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data['date_of_birth']
        dod = cleaned_data['date_of_death']
        if dob:
            self.fields['date_of_death'].widget.attrs['min'] = timezone.datetime(
                dob.year + 15, dob.month, dob.day).date().__str__()
        return cleaned_data


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
                class="btn btn-{% if object %}success{%else%}primary{% endif %} btn-lg btn-block m-1">''')
                       ),
                
                Column(HTML('''{% if object %}<button type="button"
                    class="btn btn-danger btn-lg btn-block m-1"
                    data-toggle="modal"
                    data-target="#deletemodel">
                    Delete
                    </button>{% endif %}'''),
                       id='deletebtn'
                       ) if self.initial else None,
                ),
            Row(Column(HTML('''{% if object %}<a href={% url 'system:publishermanagement' %}><i class="fas fa-arrow-circle-left"></i> Go Back</a>{%endif%}'''),
                       css_class='btn btn-link', id='goback')),
        )
        self.helper.form_id = 'bookAuthorForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = ''


class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = '__all__'
        widgets = {
            'publish_date': DateInput(),
            'rating': forms.NumberInput(),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['publish'].empty_label = 'Select Publisher'
        self.fields['author'].empty_label = 'Select Author'
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
                    'cost', '$', '.00', min=0),),
                Column(Field('page', min=0, step=1,
                             placeholder="Enter Total Pages")),
            ),
            Row(
                Column(Field('description', placeholder='Book Description',
                             maxlength=100, rows=2))
            ),
            Row(Column(Field('stock', placeholder="Total Stock"))),
            Row(Column(Field('genre'))),
            Row(Column(Field('rating', min="0", max="10",
                             step="0.5", css_class='Rangesform', title=self.instance.rating
                             ))),
            Row(Column(Field('profile', accept='image/*'))),
            Row(Column(HTML('''<input type="submit" name="{% if object %}update{%else%}{%endif%}"
                value="{% if object %}Update{%else%}Add{%endif%}"
                class="btn btn-{% if object %}success{%else%}primary{%endif%} btn-lg btn-block m-1">''')),
                Column(HTML('''<button type="button"
                class="btn btn-danger btn-lg btn-block m-1"
                data-toggle="modal"
                data-target="#deletemodel">
                Delete
                </button>''') , id='deletebtn') if self.initial else None
                ),
            Row(Column(HTML('''<a style='text-decoration:none;' href={% url 'system:bookinventory' %}><i class="fas fa-arrow-circle-left"></i> Go Back</a>'''),
                       css_class='btn btn-link')) if self.initial else None,
        )
        self.helper.form_id = 'bookForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        

class MemberForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    user_dropdown = forms.ChoiceField(choices=[(None, "Select User")]+[(user.username, f"{user.username} -> {user.email}") for user in User.objects.all()], label="Select User", required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'phone_number',
                  'state', 'city', 'pincode', 'full_address', 'profile', 'is_active']
        widgets = {
            'contactNo': forms.NumberInput(),
            'pincode': forms.NumberInput(),
            'date_of_birth': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('username', disabled=True, placeholder=_('Enter Username'))),
                Column(Field('email', disabled=True, placeholder=_('Enter Email'))),
                Column(HTML('''
                        <label>Status</label>
                        <div class="form-group">
                           <div class="input-group">
                              <button {% if request.user == object or form.is_active.value == True %}disabled{% endif %} class="form-control btn btn-success mr-1" type="submit" name="is_active" value="1"><i class="fas fa-check-circle"></i></button>
                              <button {% if request.user == object or form.is_active.value == False %}disabled{% endif %} class="form-control btn btn-warning mr-1"  type="submit" name="is_active" value="0"><i class="far fa-times-circle"></i></button>
                              <button {% if request.user == object or object.is_superuser == True %}disabled{% endif %} class="form-control btn btn-danger mr-1" type="submit" name="is_superuser" value="1"><i class="fas fa-user-check"></i></button>
                              <button {% if request.user == object or object.is_superuser == False %}disabled{% endif %} class="form-control btn btn-danger mr-1" type="submit" name="is_superuser" value="0"><i class="fas fa-user-times"></i></button>
                           </div>
                        </div>
                ''')),
            ) if self.initial else Field('user_dropdown', HTML('''
                <script>
                    document.getElementById("id_user_dropdown").onchange = event => {
                        let params = new window.URL(location);
                        const name = event.target[event.target.selectedIndex].value
                        params.search ? params.searchParams.set('username', name) : params.searchParams.append('username', name)
                        location = params
                    }
                </script>
            ''')),
            Row(
                Column(Field('first_name', disabled=True, placeholder=_('Enter First Name'))),
                Column(Field('last_name', disabled=True, placeholder=_('Enter Last Name'))),
                Column(Field('date_of_birth', disabled=True,)),
            ),
            Row(
                Column(PrependedText('phone_number', '+91', disabled=True,
                                     placeholder=_('Enter Phone Number'))),
            ),
            Field('full_address', placeholder=_('Full Address'), disabled=True,
                  maxlength=100, rows=2),
            Row(
                Column(Field('state', disabled=True)),
                Column(Field('city', disabled=True, placeholder=_('Enter Your City'))),
                Column(Field('pincode', disabled=True, placeholder=_('6 Digit pincode'))),
            ),
            Row(Column(HTML('''<button type="button"
                class="btn btn-danger btn-lg btn-block m-1"
                {% if request.user == object %}disabled{% endif %}
                data-toggle="modal"
                data-target="#deletemodel">
                Delete User Permanently
                </button>''') , id='deletebtn')) if self.initial else None,
            Row(Column(HTML('''<a href={% url 'system:membermanagement' %}><i class="fas fa-times-circle"></i> Clear Selected User</a>'''),
                       css_class='btn btn-link')) if self.initial else None,
        )
        self.helper.form_id = 'memberForm'
        self.helper.form_method = 'post'