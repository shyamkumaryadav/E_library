from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

admin.sites.AdminSite.site_header = 'E Library'


@admin.register(User)
class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email', 'is_admin', 'is_defaulter')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {
            'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'date_of_birth',
                       'contactNo', 'state', 'city', 'pincode', 'full_address', 'profile')}),
        ('Info', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')}),
        ('Permissions', {'fields': ('is_superuser',
                                    'is_admin', 'is_active', 'is_defaulter')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_superuser', 'is_admin', 'is_active', 'is_defaulter',),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('id',)
    filter_horizontal = ()

# admin.site.unregister(Group)
