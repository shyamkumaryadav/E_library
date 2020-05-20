from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages


class LogoutRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    # login_url = '/hom/t'
    goto='/view_books'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'sorry try next time')
            return redirect_to_login(self.request.get_full_path(), self.goto, self.get_redirect_field_name())

        return super().dispatch(request, *args, **kwargs)
