from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
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