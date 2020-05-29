from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings



class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is Admin or Not."""

    redirect_url = None
    permission_denied_message = 'You are Not a Admin'	
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:
            messages.warning(request, self.permission_denied_message)
            return redirect(self.login_url or settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)
