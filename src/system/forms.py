from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import password_validation as pv
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
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
	)
	password2 = forms.CharField(
		label="Password confirmation",
		validators=[password_validation],
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
		strip=False,
	)

	class Meta:
		model = MyUser
		fields = ('full_name', 'email', 'date_of_birth','contactNo','state','city','pincode','full_address','profile')
		widgets = {
			'contactNo': forms.NumberInput(
				attrs={'id':'member_id_name','class':'id_name_member test'}
			),
			'pincode': forms.NumberInput(
				attrs={'id':'pincode_test','class':'d_name_member test'}
			),
			'date_of_birth': DateInput(
				attrs={'id':'DateOfBirth','class':'id_name_member1 test1'}
			),
			'pull_address': forms.TextInput(
				attrs={'id':'pull_addres','class':'id_name_member test'}
			),
		}
		error_messages = {
			
			'pincode': {
				'invalid': 'Enter a valid Pincode',
			},
			'contactNo': {
				'invalid': 'Enter a valid Contact Number.',
			},
		}

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

	# def _post_clean(self):
	# 	super()._post_clean()
	# 	# Validate the password after self.instance is updated with form data
	# 	# by super().
	# 	password = self.cleaned_data.get('password2')
	# 	if password:
    #         try:
    #             password_validation.validate_password(password, self.instance)
    #         except ValidationError as error:
    #             self.add_error('password2', error)




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