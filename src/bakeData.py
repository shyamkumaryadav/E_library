# import requests, bs4, faker
# import os, django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_library.settings')
# django.setup()

######################################################################################################
# url = "http://127.0.0.1:8000/signup/"
# fake = faker.Faker()
# rg = requests.get(url)
# html = bs4.BeautifulSoup(rq.content, "html.parser")
# def all():
# 	for _ in html.find_all('input'): 
# 		print(f"{_['name']} : {_['type']}")

# data = { 
# 	html.input['name']:html.input['value'],
# 	'email':"admin@123.com", 
# 	'password':'as'
# }
# cookies = { 'csrftoken':html.input['value']}
# requests.post(url, data=data, headers=headers, cookies=cookies).status_code

# def makeAcc()

######################################################################################################



# url = 'https://api.covid19india.org/state_district_wise.json'
# r = requests.get(url).json()
# list_state = [key for key in r]
# # list_state_code = [r[key]['statecode'] for key in r]
# # list_states = [(None, 'Select state')]+[(j,i) for i, j in zip(list_state, list_state_code)]

# citys = { i: list(r[i]['districtData']) for i in list_state}
# # print(citys)



# from system.models import BookAuthor, BookPublish, State, City
# from faker import Faker, providers
# from random  import *

# faker = Faker()

# def AddBookAuthor(n):
# 	for i in range(n):
# 		fname = faker.name()
# 		author = BookAuthor.objects.get_or_create(name=fname)

# def AddBookPublish(n):
# 	for i in range(n):
# 		fname = faker.name()
# 		publish = BookPublish.objects.get_or_create(name=fname)

# def AddBookPublish(n):
# 	for i in range(n):
# 		fname = faker.name()
# 		publish = BookPublish.objects.get_or_create(name=fname)
# def AddCountry():
# 	for i in data: 
# 		Country.objects.get_or_create(id=i['id'],name=i['name']) 
# 		# print(f"id : {i['id']} name : {i['name']}") 

# def AddState(stateList):
# 	key = 0 
# 	for i in data: 
# 		try: 
# 			for j in i['states']: 
# 				#State.objects.get_or_create(id=i['id'],name=i['name'],country=Country.objects.get(id=i['id'])) 
# 				print(f"id={i['id']},name={j},country={Country.objects.get(id=i['id']).name}") 
# 		except KeyError: 
# 			key+=1 
# 			print('sorry!!')
# 	print('We are not abel to find some country state list = ',key)

# def AddCity():
# 	key = 0 
# 	for i in data: 
# 		try: 
# 			for j in i['states']:
# 				c_state = State.objects.filter(country__name=i['name']).filter(name=j)[0] 
# 				print(f"\nCountry: {c_state.country}, name:{c_state.name} has City ") 
# 				for c in i['states'][j]: 
# 					City.objects.get_or_create(name=c,state=c_state) 
# 					print(f"{c}\t",end="") 
# 		except KeyError: 
# 			key+=1 
# 			print('sorry!!') 


# # AddState(list_state)
# # AddCity()

# # for _ in range(len(states_code)):
# 	# print(faker.random_choices(elements=(states_code), length=1))
