from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django_otp.admin import OTPAdminSite

admin_site = OTPAdminSite(name='OTP Site')


@admin.register(User)
class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {
            'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'date_of_birth',
                       'phone_number', 'state', 'city', 'pincode', 'full_address', 'profile')}),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', 'is_superuser',
                       'is_active', 'is_staff', 'is_defaulter')}),
        ('Important dates', {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_defaulter'),
        }),
    )
