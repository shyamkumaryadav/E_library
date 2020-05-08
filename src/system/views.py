from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic.base import TemplateResponseMixin
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import UserCreationForm, UserLoginForm
from crispy_forms.utils import render_crispy_form
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from system import models
from django.contrib.auth.forms import AuthenticationForm


def home(request):
	template_name = 'system/home.html'
	context = {
		'title' : 'Home'
	}
	return render(request, template_name, context)

def about(request):
	template_name = 'system/about.html'

	context = {
		'title' : 'YouTube'
	}
	
	return render(request, template_name, context)

def terms(request):
	template_name = 'system/terms.html'
	context = {
		'title' : 'Terms',
	}
	return render(request, template_name, context)

def viewbooks(request):
	template_name = 'system/viewbooks.html'
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		form.save()
		print("hi from form sis valid")
		return redirect('system:userlogin')
	else:
		print("hi from form is not valid")
	context = {
		'title' : 'view books',
		'form' : form
	}
	return render(request, template_name, context)

def userlogin(request):
	template_name = 'system/userlogin.html'
	context = {
		'title' : 'user login'
	}
	return render(request, template_name, context)


def adminlogin(request):
	template_name = 'system/adminlogin.html'
	context = {
		'title' : 'admin login'
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
		'title' : 'sign up',
		'forms' : form,
	}
	return render(request, template_name, context)

def adminauthormanagement(request):
	template_name = 'system/adminauthormanagement.html'
	context = {
		'title' : 'admin author management'
	}
	return render(request, template_name, context)
	
def adminmembermanagement(request):
	template_name = 'system/adminmembermanagement.html'
	context = {
		'title' : 'admin member management'
	}

	return render(request, template_name, context)

def adminbookissuing(request):
	template_name = 'system/adminbookissuing.html'
	context = {
		'title' : 'admin book issuing'
	}
	return render(request, template_name, context)

def adminbookinventory(request):
	template_name = 'system/adminbookinventory.html'
	context = {
		'title' : 'admin book inventory'
	}
	return render(request, template_name, context)

def adminpublishermanagement(request):
	template_name = 'system/adminpublishermanagement.html'
	context = {
		'title' : 'admin publisher management'
	}
	return render(request, template_name, context)

def shyamkumaryadav(request):
	template_name = 'system/shyamkumaryadav.html'
	context = {
		'title' : 'shyamkumar yadav'
	}
	return render(request, template_name, context)
class AuthorUpdate(UpdateView):
	model = models.MyUser
	fields = ('__all__')

def handler404(request, *args, **argv):
	return HttpResponseNotFound(f"<h1>This Page <br><u>{request.is_secure()}</u><br> you are not find this on page</h1>")
def handler500(request, *args, **argv):
	return HttpResponseNotFound(f"<h1>This Page <br><u>{request}</u><br> you are not find this on page</h1>")