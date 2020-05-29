from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages


class LogoutRequiredMixin(AccessMixin):
    """Verify that the current user is Not authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 
            	'You have Already Account to Make New Accout Plz <a href="/account/logout/">Logout</a> ')
            return redirect('system:viewbooks')

        return super().dispatch(request, *args, **kwargs)
