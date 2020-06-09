from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django_otp.admin import OTPAdminSite

admin_site = OTPAdminSite(name='OTP Site')

@admin.register(User)
class UserAdmin( BaseUserAdmin, ImportExportModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_defaulter')
    list_filter = ('is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {
            'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'date_of_birth',
                       'contactNo', 'state', 'city', 'pincode', 'full_address', 'profile')}),
        ('Permissions', {'fields': ('groups', 'user_permissions','is_superuser',
                                    'is_admin', 'is_active', 'is_defaulter')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_superuser', 'is_admin', 'is_active', 'is_defaulter',),
        }),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
