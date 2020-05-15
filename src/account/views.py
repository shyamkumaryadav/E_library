from django.shortcuts import render, redirect
from django.views.generic import View
from django import views
from django.contrib.auth import login, logout


def user_logout(request):
    logout(request)
    return redirect('system:home')


def user_login(request):
    login(request, *args, **kwargs)


class Login():
	template_name = "login.html"
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
