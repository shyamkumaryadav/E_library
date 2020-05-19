from django.shortcuts import render, redirect
from django.views import generic
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    JsonResponse
)
from django.urls import reverse
from django.contrib.auth import login
from crispy_forms.utils import render_crispy_form
from account.forms import UserCreationForm, UserLoginForm
from system import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from account.models import User
from .models import Book


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


@login_required
def terms(request):
    template_name = 'system/terms.html'
    messages.add_message(request, messages.INFO, 'Hello world.')
    context = {
        'title': 'Terms',
    }
    return render(request, template_name, context)


class ViewBookView(generic.ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 6
    template_name = 'system/viewbooks.html'


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
