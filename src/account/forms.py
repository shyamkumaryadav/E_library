from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import (
    authenticate, get_user_model, password_validation
)
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
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
        help_text='''
            Your password can’t be too similar to your other personal information.<br>
            Your password must contain at least 8 characters.<br>
            Your password can’t be a commonly used password.<br>
            Your password can’t be entirely numeric.<br>
        '''
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Same Password', 'autocomplete': 'new-password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'date_of_birth', 'contactNo',
                  'state', 'city', 'pincode', 'full_address', 'profile')
        widgets = {
            'contactNo': forms.NumberInput(),
            'pincode': forms.NumberInput(),
            'date_of_birth': DateInput(),
            'profile': forms.FileInput(),
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
            Field('username'),
            Field('email'),
            Row(
                Column(Field('first_name')),
                Column(Field('last_name')),
            ),
            Row(
                Column(Field('date_of_birth', type="date")),
                Column(Field('contactNo')),
            ),
            Field('state'),
            Row(
                Column(Field('city')),
                Column(Field('pincode')),
            ),
            Field('full_address', placeholder='Full Address',
                  maxlength=100, rows=3),
            Field('profile', ),
            Field('password1'),
            Field('password2'),
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
    name = forms.CharField(
        label="Username or Email",
        # widget=forms.TextInput(
        #     attrs={'placeholder': "Enter Username or Email"})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': "current-password", 'placeholder': "Enter Password"}),
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column(Field('name', placeholder="Enter Username or Email")),
            Column(AppendedText('password',
                                '<div class="input-group-addon">\
                    <a href="" id="show_hide_password"><i class="fa fa-eye-slash" aria-hidden="true"></i></a>\
                </div>'
                                )),
            Div(Submit('submit', 'Login', css_class="btn-block btn-lg"),
                css_class='text-center m-4'),
            Div(HTML('<input type="button" name="signup" value="signup" class="btn btn btn-info btn-block btn-lg" id="button-id-signup" onclick="location.href=\'{% url \'account:signup\'%}\'">'),
                css_class='text-center m-4'),
            HTML('''<script>
                $(document).ready(function() {
                    $("#show_hide_password").on('click', function(event) {
                    event.preventDefault();
                    if($('#id_password').attr("type") == "text"){
                        $('#id_password').attr('type', 'password');
                        $('#show_hide_password i').addClass( "fa-eye-slash" );
                        $('#show_hide_password i').removeClass( "fa-eye" );
                    }else if($('#id_password').attr("type") == "password"){
                        $('#id_password').attr('type', 'text');
                        $('#show_hide_password i').removeClass( "fa-eye-slash" );
                        $('#show_hide_password i').addClass( "fa-eye" );
                    }
                });
            });
            </script>''')
        )
        self.helper.form_id = 'LoginForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

    def clean(self):
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get("password")
        try:
            if name.find('@' and '.') != -1:
                name = User.objects.get(email=name).username
        except:
            raise forms.ValidationError(
                "Please enter a correct email and password."
                " Note that both fields may be case-sensitive.")
        if name is not None and password:
            self.user_cache = authenticate(
                self.request, username=name, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct username and password."
                    " Note that both fields may be case-sensitive.")
            else:
                if not self.user_cache.is_active:
                    raise forms.ValidationError("This account is inactive.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
