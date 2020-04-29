import requests

url = 'https://api.covid19india.org/state_district_wise.json'

from django.shortcuts import render
from . import forms, models
from apiclient.discovery import build                                                           

api_key = 'AIzaSyDrecpXxZFguNK9-yW__Xmk-g4qFB1hwfE'                                             
youtube = build('youtube','v3', developerKey=api_key) 



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
	if request.GET.get('q'):
		req = youtube.search().list(q=request.GET.get('q'), part="snippet", type="channel")
		context.update({'data':req.execute()})
	return render(request, template_name, context)

def terms(request):
	template_name = 'system/terms.html'
	form = forms.UserLoginForm()
	model = models.State.objects.all()
	context = {'title' : 'terms',
				'form' : form,
				'model' : model
	}
	if request.GET.get('state'):
		r = dict(requests.get(url).json())
		code = request.GET.get('state')
		for _ in r:
			if r[_]['statecode'] == code:
				context.update({'data':r[_]})
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