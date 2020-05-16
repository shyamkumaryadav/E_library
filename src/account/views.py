from django.shortcuts import render, redirect
from django import views
from django.conf import settings
from django.contrib.auth import login, logout


def user_logout(request):
    logout(request)
    return redirect('system:home')


def user_login(request):
    login(request, *args, **kwargs)


class Logout(views.View):
    template_name = "logout.html"

    def get(self, request):
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)

    def post(self, request):
        pass
