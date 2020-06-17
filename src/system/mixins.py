from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.conf import settings


class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is Admin or Not."""

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                messages.warning(request, 'You Are Not Admin?')
                return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_admin:
    #         messages.warning(request, self.permission_denied_message)
    #         return redirect_to_login(self.request.get_full_path(), settings.LOGIN_URL, self.get_redirect_field_name())
    #     return super().dispatch(request, *args, **kwargs)
