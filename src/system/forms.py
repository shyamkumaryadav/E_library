from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import password_validation as pv
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
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
		# validators=[password_validation],
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
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
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

		)
		self.helper.form_id = 'userCreationForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = ''
		self.helper.add_input(Submit('submit', 'Sign Up'))




class UserChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = MyUser
		fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial["password"]


# labels = {
#     'name': 'Writer',
# }
# widgets = {
#     'name': forms.TextInput(attrs={'id':'member_id_name','class':'id_name_member test'}),
# }
# error_messages = {
#     'name': {
#         'max_length': "This writer's name is too long.",
# 	},
# }