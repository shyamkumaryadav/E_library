from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout


def user_logout(request):
    logout(request)
    return redirect('system:home')
