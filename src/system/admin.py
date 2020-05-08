from .models import (
	Book,
	Issue,
	BookAuthor,
	BookPublish,
	MyUser,
	Genre,
)
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('email', 'id', 'is_admin','is_active')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('full_name', 'date_of_birth','contactNo','state','city','pincode','full_address','profile')}),
		('Permissions', {'fields': ('is_admin','is_active', )}),
		('Important dates', {'fields': ('last_login',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('full_name', 'email','date_of_birth','contactNo','state','city','pincode','full_address', 'password1', 'password2','profile'),
		}),
	)
	search_fields = ('email',)
	ordering = ('id',)
	filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
class BookAdmin(admin.ModelAdmin):
	list_display = ('bookid', 'name','author', 'language', 'display_genre','stock','today_stock')
	search_fields = ('name',)
	ordering = ('bookid',)
	list_filter = ('genre', 'language',)


admin.site.register(Book, BookAdmin)
admin.site.register(Issue)
admin.site.register(BookAuthor)
admin.site.register(BookPublish)
admin.site.register(Genre)
