from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
    PasswordResetView)
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserLoginForm, UserCreationForm, UserChangeForm
from system.mixins import AdminRequiredMixin
from .mixins import LogoutRequiredMixin, AdminSameRequiredMixin
from django_otp.forms import OTPAuthenticationForm
from .models import User
from .token import token_generator
from django.utils.http import urlsafe_base64_decode
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/form_.html'
    # redirect_authenticated_user = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('admin') and (int(self.request.GET.get('admin')) == 1):
            context['title'] = 'Admin Login'
        else:
            context['title'] = 'User Login'
        return context

class UserCreateView(LogoutRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    extra_context = {'title' : _("User Signup")}

    def form_valid(self, form):
        form.save(request=self.request)
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Your Profile Create Success. You received a email to activate Your account.')
        return reverse_lazy('account:signin')

class UserEmailVerified(TemplateView):
    template_name = "account/email.html"

    def dispatch(self, request, *args, **kwargs):
        assert 'uid' in kwargs and 'token' in kwargs
        self.validlink = False
        self.token = False
        self.user = self.get_user(kwargs['uid'])
        if self.user is not None:
            if token_generator.check_token(self.user, kwargs['token']):
                self.token = True
                if not self.user.is_active: 
                    self.user.is_active = True
                    self.validlink = True
                    self.user.save()
        return super().dispatch(request, *args, **kwargs)
    
    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.token:
            context['user'] = self.user
        if self.validlink:
             context.update({
                'title': _('Email verified successful'),
                'validlink': True,
            })
        else:
            context.update({
                'title': _('Email verified unsuccessful'),
                'validlink': False,
            })
        return context



class UserLogoutView(LogoutView):
    template_name = 'account/logout.html'
    redirect_authenticated_user = True


class UserUpdateView(AdminSameRequiredMixin, UpdateView):
    next_page = reverse_lazy('account:signin')
    model = User
    form_class = UserChangeForm
    template_name = 'account/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        messages.success(self.request, 'Your Profile Update success.')
        return reverse_lazy('account:update', kwargs={'username': self.request.user.username})


class UserPasswordResetView(LogoutRequiredMixin, PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    html_email_template_name = 'account/password_reset_email.html'
    template_name = 'account/password_reset_form.html'
    title = 'Password reset'

    def get_success_url(self):
        messages.success(self.request, "We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly.")
        messages.info(self.request, "If you don’t receive an email, please make sure you’ve entered the address you registered with, and check your spam folder.")
        return reverse_lazy('account:signin')


class UserPasswordResetConfirmView(LogoutRequiredMixin, PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'

    def get_success_url(self):
        messages.success(self.request, 'Your Password Change success.')
        return reverse_lazy('account:signin')

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Your Password Change success.')
        return reverse_lazy('account:update', kwargs={'username': self.request.user.username})
