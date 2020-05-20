from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserLoginForm, UserCreationForm
from .mixins import LogoutRequiredMixin


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = False


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('account:signin')
    template_name = 'account/logout.html'
    redirect_authenticated_user = False


class AjaxableResponseMixin:

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            print(form.errors)
            return JsonResponse(form.errors, status=400)
        else:
            print(response)
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class UserCreateView(LogoutRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('system:home')
    #     else:
    #         return super().get(request, *args, **kwargs)
