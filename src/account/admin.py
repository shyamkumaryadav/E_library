from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email', 'is_admin', 'is_defaulter')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth',
                                      'contactNo', 'state', 'city', 'pincode', 'full_address', 'profile')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_defaulter')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'date_of_birth', 'contactNo', 'state', 'city', 'pincode', 'full_address', 'password1', 'password2', 'profile'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)
