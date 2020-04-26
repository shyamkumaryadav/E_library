import requests
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_library.settings')
django.setup()


url = 'https://api.covid19india.org/state_district_wise.json'
r = requests.get(url).json()
list_state = [key for key in r]
# list_state_code = [r[key]['statecode'] for key in r]
# list_states = [(None, 'Select state')]+[(j,i) for i, j in zip(list_state, list_state_code)]

citys = { i: list(r[i]['districtData']) for i in list_state}
# print(citys)



from system.models import BookAuthor, BookPublish, State, City
from faker import Faker, providers
from random  import *

faker = Faker()

def AddBookAuthor(n):
	for i in range(n):
		fname = faker.name()
		author = BookAuthor.objects.get_or_create(name=fname)

def AddBookPublish(n):
	for i in range(n):
		fname = faker.name()
		publish = BookPublish.objects.get_or_create(name=fname)

def AddBookPublish(n):
	for i in range(n):
		fname = faker.name()
		publish = BookPublish.objects.get_or_create(name=fname)

def AddState(stateList):
	stateList.sort()
	for i in stateList:
		s_id = r[i]['statecode']
		s_name = i
		State.objects.get_or_create(state_id=s_id, name=s_name)

def AddCity():
	list_state.sort()
	for i in list_state:
		for j in citys[i]:
			if j=="Unknown":
				continue	
			f_name = j
			f_state = State.objects.get(state_id=r[i]['statecode'])
			City.objects.create(name = f_name, state = f_state)

AddState(list_state)
AddCity()

# for _ in range(len(states_code)):
	# print(faker.random_choices(elements=(states_code), length=1))
