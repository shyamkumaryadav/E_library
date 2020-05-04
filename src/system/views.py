from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound

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
	context = {
		'title' : 'view books'
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
	context = {
		'title' : 'sign up'
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


def handler404(request, *args, **argv):
	return HttpResponseNotFound("i thin you are not find this on page")