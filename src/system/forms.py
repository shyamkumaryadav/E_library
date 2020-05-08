from django import forms
from django.contrib.auth.forms import (
	ReadOnlyPasswordHashField,
	AuthenticationForm,
	UsernameField
)
from django.contrib.auth import password_validation as pv
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
	Layout,
	Submit,
	Row,
	Column,
	Fieldset,
	ButtonHolder,
	HTML,
	Div,
)
from django.core.exceptions import ValidationError
from .models import MyUser

class DateInput(forms.DateInput):
	input_type='date'

def password_validation(value):
	pv.validate_password(value)


class UserCreationForm(forms.ModelForm):
	"""A form for creating new users. Includes all the required
	fields, plus a repeated password."""
	password1 = forms.CharField(
		label="Password",
		strip=False,
		validators=[password_validation],
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password','autocomplete': 'new-password'}),
	)
	password2 = forms.CharField(
		label="Password confirmation",
		validators=[password_validation],
		widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Same Password','autocomplete': 'new-password'}),
		strip=False,
	)
	class Meta:
		model = MyUser
		fields = ('full_name', 'email', 'date_of_birth','contactNo',
		'state','city','pincode','full_address','profile')
		widgets = {
			'full_name': forms.TextInput(
				attrs={'class':'form-control invalid','aria-describedby':"passwordHelpBlock", 'placeholder':'Enter Full Name'}
			),
			'email': forms.EmailInput(
				attrs={'class':'form-control', 'placeholder':'Enter Email Address'}
			),
			'contactNo': forms.NumberInput(
				attrs={'class':'form-control', 'placeholder':'Enter Contact Number'}
			),
			'pincode': forms.NumberInput(
				attrs={'class':'form-control', 'placeholder':'Enter 6 digit PinCode'}
			),
			'city': forms.TextInput(
				attrs={'class':'form-control', 'placeholder':'Enter City'}
			),
			'state': forms.Select(
				attrs={'class':'form-control'}
			),
			'date_of_birth': DateInput(
				attrs={'class':'form-control'}
			),
			'full_address': forms.Textarea(
				attrs={'class':'form-control','placeholder':'Full Address', 'maxlength':10,'rows':5}
			),
			'profile': forms.FileInput(
				attrs={'class':'custom-file-input'}
			),
		}
		error_messages = {}
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2
	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
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
			Div(ButtonHolder(Submit('submit', 'Sign Up')), css_class='text-center'),
		)
		self.helper.form_id = 'userCreationForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = ''
		# self.helper.add_input(Submit('submit', 'Sign Up'))

class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField(
		label="Password",
        help_text='Raw passwords are not stored, so there is no way to see this '
            'user’s password, but you can change the password using '
            '<a href="{}">this form</a>.',
	)
	class Meta:
		model = MyUser
		fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		password = self.fields.get('password')
		if password:
			password.help_text = password.help_text.format('../password/')
		user_permissions = self.fields.get('user_permissions')
		if user_permissions:
			user_permissions.queryset = user_permissions.queryset.select_related('content_type')

	def clean_password(self):
		return self.initial["password"]

class UserLoginForm(AuthenticationForm):

	username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder':'Enter Your Email'}))
	password = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','placeholder':'Enter Password'}),
	)

	error_messages = {
		'invalid_login': "Please enter a correct %(username)s and password. Note that both "
		"fields may be case-sensitive.",
		'inactive': "This account is inactive.",
	}

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Column('username'),
			Column('password'),
			Fieldset(
				'first arg is the legend of the fieldset',
				'like_website',
				'favorite_number',
				'favorite_color',
				HTML("""
					<p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
				"""),
				'favorite_food',
				'notes'
			),
			ButtonHolder(
				Submit('', 'HI', css_class='button white')
		)
		)
		self.helper.form_id = 'userLoginForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = ''
		self.helper.add_input(Submit('submit', 'Login'))