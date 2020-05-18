from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import (
    authenticate, get_user_model, password_validation
)
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField,
    AuthenticationForm,
    UsernameField
)
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        validators=[password_validation.validate_password],
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Same Password', 'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('full_name', 'email', 'date_of_birth', 'contactNo',
                  'state', 'city', 'pincode', 'full_address', 'profile')
        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control invalid',
                       'aria-describedby': "passwordHelpBlock", 'placeholder': 'Enter Full Name'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Email Address'}
            ),
            'contactNo': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Contact Number'}
            ),
            'pincode': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 6 digit PinCode'}
            ),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter City'}
            ),
            'state': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'date_of_birth': DateInput(
                attrs={'class': 'form-control'}
            ),
            'full_address': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Full Address', 'maxlength': 10, 'rows': 5}
            ),
            'profile': forms.FileInput(
                attrs={'class': 'custom-file-input'}
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('full_name'),
                Column('email'),
            ),
            Row(
                Column('date_of_birth'),
                Column('contactNo'),
            ),
            'state',
            Row(
                Column('city'),
                Column('pincode'),
            ),
            'full_address',
            'profile',
            'password1',
            'password2',
            Div(Submit('submit', 'Sign Up'), css_class='text-center'),
        )
        self.helper.form_id = 'userCreationForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text='Raw passwords are not stored, so there is no way to see this '
        'user’s password, but you can change the password using '
        '<a href="{}">this form</a>.',
    )

    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                'content_type')

    def clean_password(self):
        return self.initial["password"]


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(),
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column(Field('email', placeholder="Enter Email")),
            Column(Field('password', placeholder="Enter Password")),
            Div(Submit('submit', 'Login', css_class="btn-block btn-lg"),
                css_class='text-center m-4'),
            Div(HTML('<input type="button" name="signup" value="signup" class="btn btn btn-info btn-block btn-lg" id="button-id-signup" onclick="location.href=\'{% url \'system:signup\'%}\'">'),
                css_class='text-center m-4')
        )
        self.helper.form_id = 'LoginForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get("password")
        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct email and password."
                    "Note that both fields may be case-sensitive.")
            else:
                if not self.user_cache.is_active:
                    raise forms.ValidationError("This account is inactive.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
