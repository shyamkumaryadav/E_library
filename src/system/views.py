from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import login
from crispy_forms.utils import render_crispy_form
from account.forms import UserCreationForm, UserLoginForm
from system import models
from account.models import User
from account.forms import AuthenticationForm


def home(request):
    template_name = 'system/home.html'
    context = {
        'title': 'Home'
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'system/about.html'
    context = {
        'title': 'About'
    }
    return render(request, template_name, context)


def terms(request):
    template_name = 'system/terms.html'
    context = {
        'title': 'Terms',
    }
    return render(request, template_name, context)


def viewbooks(request):
    template_name = 'system/viewbooks.html'
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('system:home')
    else:
        form = UserLoginForm(None)
    context = {
        'title': 'view books',
        'form': form
    }
    return render(request, template_name, context)


def userlogin(request):
    template_name = 'system/userlogin.html'
    forms = UserLoginForm(request.POST or None)
    if forms.is_valid():
        login(request, forms.get_user())
        return redirect('system:home')
    context = {
        'title': 'user login',
        'form': forms
    }
    return render(request, template_name, context)


def adminlogin(request):
    template_name = 'system/adminlogin.html'
    context = {
        'title': 'admin login'
    }

    return render(request, template_name, context)


def signup(request):
    template_name = 'system/signup.html'
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("hi from form sis valid")
        return redirect('system:userlogin')
    else:
        print("hi from form is not valid")
    context = {
        'title': 'sign up',
        'forms': form,
    }
    return render(request, template_name, context)


def adminauthormanagement(request):
    template_name = 'system/adminauthormanagement.html'
    context = {
        'title': 'admin author management'
    }
    return render(request, template_name, context)


def adminmembermanagement(request):
    template_name = 'system/adminmembermanagement.html'
    context = {
        'title': 'admin member management'
    }

    return render(request, template_name, context)


def adminbookissuing(request):
    template_name = 'system/adminbookissuing.html'
    context = {
        'title': 'admin book issuing'
    }
    return render(request, template_name, context)


def adminbookinventory(request):
    template_name = 'system/adminbookinventory.html'
    context = {
        'title': 'admin book inventory'
    }
    return render(request, template_name, context)


def adminpublishermanagement(request):
    template_name = 'system/adminpublishermanagement.html'
    context = {
        'title': 'admin publisher management'
    }
    return render(request, template_name, context)


def shyamkumaryadav(request):
    template_name = 'system/shyamkumaryadav.html'
    context = {
        'title': 'shyamkumar yadav'
    }
    return render(request, template_name, context)
