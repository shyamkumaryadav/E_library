from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
    PasswordResetView)
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserLoginForm, UserCreationForm
from .mixins import LogoutRequiredMixin
from django_otp.forms import OTPAuthenticationForm



class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = False
    # authentication_form=OTPAuthenticationForm


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('account:signin')
    template_name = 'account/logout.html'
    redirect_authenticated_user = False

class UserPasswordResetView(PasswordResetView):
    email_template_name = ''
    extra_email_context = None
    # form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    # subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')
    template_name = 'account/password_reset_form.html'
    title = 'Password reset'
    # token_generator = default_token_generator

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    # form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = 'set-password'
    success_url = reverse_lazy('account:password_reset_complete')
    template_name = 'account/password_reset_confirm.html'
    # title = _('Enter new password')
    # token_generator = default_token_generator

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
    template_name = 'account/password_change_form.html'

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'


class UserCreateView(LogoutRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('system:home')
    #     else:
    #         return super().get(request, *args, **kwargs)

def test(request, token):
    if token == 'ji-set':
        return HttpResponse('hello '+ token)
    return HttpResponseRedirect(request.path.replace(token, 'ji-set'))