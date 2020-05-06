from .models import (
	Book,
	Issue,
	BookAuthor,
	BookPublish,
)
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = UserChangeForm
	add_form = UserCreationForm

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('email', 'is_admin','is_active')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('full_name', 'date_of_birth','contactNo','state','city','pincode','full_address','profile')}),
		('Permissions', {'fields': ('is_admin','is_active')}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('full_name', 'email','date_of_birth','contactNo','state','city','pincode','full_address', 'password1', 'password2','profile'),
		}),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(BookAuthor)
admin.site.register(BookPublish)
