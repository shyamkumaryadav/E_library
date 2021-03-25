from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import (
    authenticate, get_user_model, password_validation
)
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from django.contrib.auth.forms import (
    AuthenticationForm,
    ReadOnlyPasswordHashField,
    ReadOnlyPasswordHashWidget,
    UsernameField
)
from django.urls import reverse_lazy
from .models import User
from .token import send_mail
from django.utils.translation import gettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'


class HD(ReadOnlyPasswordHashWidget):
    template_name = 'account/widgets/read_only_password_hash.html'


class UserCreationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        validators=[password_validation.validate_password],
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        validators=[password_validation.validate_password],
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('Enter Same Password'), 'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('username', 'email', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True, request=None):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        user.is_active = False
        if commit and request:
            send_mail(user, request=request)
            user.save()
        return user
    
    

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.auto_id = '%s'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('username', placeholder=_('Enter Username'))),
                Column(Field('email', placeholder=_('Enter Email'))),
            ),
            Row(
                Column(Field('password1')),
                Column(Field('password2'))
            ),
            Div(Submit('submit', 'Sign Up', css_class='btn-lg',),
                css_class='text-center'),
            HTML('''
                <style>
                   #hint_password1>ul{
                        list-style: none;
                        padding-left: 0;
                    }
                </style>
            '''),
            HTML('<p class="text-muted text-center m-4" >Already have an account ? <a class="text-monospace text-uppercase text-decoration-none text-success" href={% url "account:signin" %}>Login</a></p>')
        )
        self.helper.form_method = 'post'


class UserChangeForm(forms.ModelForm):
    password = forms.CharField(
        label=_("Password"),
        disabled=True,
        required=False,
        initial='*'*16,
        help_text=_('Raw passwords are not stored, so there is no way to see your '
                'password, but you can change the password using '
                '<a href="{}">this link</a>.')
        # widget=HD(),
    )
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'phone_number',
                  'state', 'city', 'pincode', 'full_address', 'profile']
        widgets = {
            'contactNo': forms.NumberInput(),
            'pincode': forms.NumberInput(),
            'date_of_birth': DateInput(),
            # 'profile': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format(reverse_lazy('account:password'))
        # user_permissions = self.fields.get('user_permissions')
        # if user_permissions:
        #     user_permissions.queryset = user_permissions.queryset.select_related(
        #         'content_type')
        self.auto_id = '%s'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('username', placeholder=_('Enter Username'))),
                Column(Field('email', placeholder=_('Enter Email'))),
            ),
            Row(
                Column(Field('first_name', placeholder=_('Enter First Name'))),
                Column(Field('last_name', placeholder=_('Enter Last Name'))),
            ),
            Row(
                Column(Field('date_of_birth')),
                Column(PrependedText('phone_number', '+91',
                                     placeholder=_('Enter Phone Number'))),
            ),
            Field('full_address', placeholder=_('Full Address'),
                  maxlength=100, rows=2),
            Row(
                Column(Field('state')),
                Column(Field('city')),
                Column(Field('pincode', placeholder=_('6 Digit pincode'))),
            ),
            Field('profile', accept='image/*', placeholder='Open File'),
            Div(Field('password')),
            Div(Submit('value', _('Update'), css_class='btn-lg',),
                css_class='text-center'),
        )
        self.helper.form_id = 'userChangeForm'
        self.helper.form_method = 'post'


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username', placeholder="Enter Your Username"),
            AppendedText('password',
                '<i id="eye" class="fa fa-eye-slash" aria-hidden="true"></i>', placeholder="Enter Your Password"),
            HTML('''
                <script>
                   document.getElementById('div_id_password').children[1].children[0].children[1].children[0].addEventListener('click', (e) => {
                      const eye = document.getElementById('eye').classList;
                      eye.toggle("fa-eye")
                      eye.toggle("fa-eye-slash")
                      const id_password = document.getElementById('id_password');
                      if(id_password.type == "text"){
                         id_password.type = 'password';
                      }else if(id_password.type == "password"){
                         id_password.type = 'text';
                      }
                   });
                </script>
            '''),
            HTML('<a class="badge mb-2 p-1" href={% url "account:password_reset" %}>Forget Password ?</a>'),
            Div(Submit('submit', 'Log In', css_class="btn btn-lg"),css_class='text-center'),
            HTML('<p class="text-muted text-center m-4" >New To E-library ? <a class="text-monospace text-uppercase text-decoration-none text-success" href={% url "account:signup" %}>Sign up</a></p>')
        )
        self.helper.form_method = 'POST'
