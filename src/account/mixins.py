from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class LogoutRequiredMixin(AccessMixin):
	"""Verify that the current user is Not authenticated."""
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			messages.add_message(request, 100,
				_('You have Already Login. To Visit <a href="{0}">{0}</a> path <a href="{1}">logout</a>').format(request.path, reverse_lazy('account:logout')),
				extra_tags='danger')
			return redirect('system:home')

		return super().dispatch(request, *args, **kwargs)


class AdminSameRequiredMixin(AccessMixin):
	"""Verify that the current user is Admin or Not."""

	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
				messages.add_message(request, 100,
					_('You Are Not Authenticated?'), extra_tags='danger')
				return self.handle_no_permission()
		if request.user.is_authenticated:
			if request.user.username != kwargs['username']:
				messages.add_message(request, 50,
					_('You are not able to Update Your Profile use <a href={}>this</a> link to update?').format(reverse_lazy('account:update', kwargs = {'username': request.user.username})),
					extra_tags='primary')
				return redirect('system:home')
		return super().dispatch(request, *args, **kwargs)
