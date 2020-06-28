from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages


class LogoutRequiredMixin(AccessMixin):
	"""Verify that the current user is Not authenticated."""
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			messages.add_message(request, 100,
				'You have Already Account to Make New Accout Plz <a href={}>Logout</a>?'.format(reverse_lazy('account:logout')),
				extra_tags='danger')
			return redirect('system:viewbooks')

		return super().dispatch(request, *args, **kwargs)


class AdminSameRequiredMixin(AccessMixin):
	"""Verify that the current user is Admin or Not."""

	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
				messages.add_message(request, 100,
					'You Are Not Authenticated?', extra_tags='danger')
				return self.handle_no_permission()
		if request.user.is_authenticated:
			if request.user.username != kwargs['username']:
				messages.add_message(request, 50,
					'You are not able to Update Profile use <a href={}>this</a> link to update?'.format(reverse_lazy('account:update', kwargs = {'username': request.user.username})),
					extra_tags='primary')
				return redirect('system:home')
		return super().dispatch(request, *args, **kwargs)