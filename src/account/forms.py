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
from django_otp.forms import OTPAuthenticationFormMixin
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserCreationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
    }
    password1 = forms.CharField(
        label="Password",
        strip=False,
        validators=[password_validation.validate_password],
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html()
        # '''
        #     Your password can’t be too similar to your other personal information.<br>
        #     Your password must contain at least %(max_length) characters.<br>
        #     Your password can’t be a commonly used password.<br>
        #     Your password can’t be entirely numeric.<br>
        # '''
    )
    password2 = forms.CharField(
        label="Password confirmation",
        validators=[password_validation.validate_password],
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
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.auto_id = '%s'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(Field('username', placeholder='Enter Username')),
                Column(Field('email', placeholder='Enter Email')),
            ),
            Row(
                Column(Field('first_name', placeholder='Enter First Name')),
                Column(Field('last_name', placeholder='Enter Last Name')),
            ),
            Row(
                Column(Field('date_of_birth')),
                Column(Field('contactNo', placeholder='Enter Phone Number')),
            ),
            Row(
                Column(Field('state')),
                Column(Field('city')),
                Column(Field('pincode', placeholder='6 Digit pincode')),
            ),
            Field('full_address', placeholder='Full Address',
                  maxlength=100, rows=2),
            Field('profile'),
            Row(
                Column(Field('password1')),
                Column(Field('password2'))
            ),
            Div(Submit('submit', 'Sign Up', css_class='btn-lg',),
                css_class='text-center'),
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


class UserLoginForm(OTPAuthenticationFormMixin, AuthenticationForm):
    otp_error_messages = dict(OTPAuthenticationFormMixin.otp_error_messages,
                              challenge_message='{0}',
                              challenge_exception='Error generating challenge. Please try again.',
                              )

    otp_device = forms.CharField(
        required=False, widget=forms.Select)
    otp_token = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    otp_challenge = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            Field('otp_challenge', type='hidden')
        )
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        # try:
        self.cleaned_data = super().clean()

        if super().get_user():
            self.helper[0:2].wrap(Field, type='hidden')
            # if self.cleaned_data['otp_token'] != '':
            print(self.device_choices(super().get_user()))
            # try:
            #     self.cleaned_data['otp_device'] = self.device_choices(
            #         super().get_user())[0][0]
            # except:
            #     pass
            self.cleaned_data['otp_challenge'] = 'otp' if self.cleaned_data['otp_token'] == '' else ''
            if len(self.device_choices(super().get_user())) > 1:
                self.helper.layout.append(Field('otp_device'))
            else:
                self.cleaned_data['otp_device'] = self.device_choices(
                    super().get_user())[0][0]
            self.helper.layout.append(
                Field('otp_token', placeholder='Enter Your OTP...'))
            # self.helper.layout.append(Field('otp_device'))
            # self.helper.layout.append(Field('otp_challenge'))
            # print(self.cleaned_data)
            # self.helper.add_input(Submit('otp_challenge', 'Get OTP'))
        print(self.cleaned_data)
        self.clean_otp(self.get_user())

        return self.cleaned_data

# class UserLoginForm(OTPAuthenticationFormMixin, forms.Form):
#     name = forms.CharField()
#     password = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={'autocomplete': "current-password", 'placeholder': "Enter Password"}),
#     )
#     otp_device = forms.CharField(required=False, widget=forms.Select)
#     otp_token = forms.CharField(
#         required=False, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
#     otp_challenge = forms.CharField(required=False)

#     def __init__(self, request=None, *args, **kwargs):
#         self.request = request
#         self.user_cache = None
#         super().__init__(auto_id='%s', *args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Column(Field('name', placeholder="Enter Username or Email")),
#             Column(AppendedText(
#                 'password', '<i id="eye" class="fa fa-eye-slash" aria-hidden="true"></i>')),
#             # '<div  class="input-group-addon" style="background-color:transparent !important;">\
#             # ),
#             Column(Field('otp_device')),
#             # Column(Field('otp_challenge')),
#             Column(Field('otp_token', placeholder="Enter OTP")),
#             Div(Submit('submit', 'Sign In', css_class="btn-block btn-lg"),
#                 css_class='text-center m-4',
#             Div(Submit('otp_callenge', 'Get Challenge', css_class="btn-block btn-lg"),
#                 css_class='text-center m-4'),
#         )
#         # {% if form.get_user %}<input type="submit" name="otp_challenge" class='btn btn-info' value="Get Challenge" />{% endif %}

#         self.helper.form_id = 'LoginForm'
#         self.helper.form_class = 'blueForms'
#         self.helper.form_method = 'post'
#         self.helper.form_action = ''

#     def clean(self):
#         self.cleaned_data = super().clean()
#         name = self.cleaned_data.get('name')
#         password = self.cleaned_data.get("password")
#         try:
#             if name.find('@' and '.') != -1:
#                 name = User.objects.get(email=name).username
#         except:
#             raise forms.ValidationError(
#                 "Please enter a correct email and password."
#                 " Note that both fields may be case-sensitive.")
#         if name is not None and password:
#             self.user_cache = authenticate(
#                 self.request, username=name, password=password)
#             if self.user_cache is None:
#                 raise forms.ValidationError(
#                     "Please enter a correct username and password."
#                     " Note that both fields may be case-sensitive.")
#             else:
#                 if not self.user_cache.is_active:
#                     raise forms.ValidationError(
#                         "This account is inactive. Contact to Admin")
#         self.clean_otp(self.get_user())
#         return self.cleaned_data

#     def get_user(self):
#         return self.user_cache
