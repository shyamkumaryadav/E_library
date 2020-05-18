from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserLoginForm, UserCreationForm


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'account/logout.html'


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('system:home')
        else:
            return super().get(request, *args, **kwargs)
