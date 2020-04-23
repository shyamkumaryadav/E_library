import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_library.settings')
django.setup()



from system.models import BookAuthor, BookPublish, states
from faker import Faker, providers
from random  import *

faker = Faker(['hi_IN'])

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


states_code = ('AP', 'AR', 'AS', 'BR', 'CT', 'GA', 'HR', 'HP', 'JH', 'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OR', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UT', 'UP', 'WB', 'AN', 'CH', 'DB', 'DD', 'DL', 'JK', 'LA', 'LD')

# a=0
# for _ in range(len(states_code)):
# 	# print(faker.random_choices(elements=(states_code), length=1)[0])
# 	a+=1

# print(a)


# def AddBook(n):
# 	for i in range(n):
# 		fname
# 		fusername
# 		fbirthday
# 		phone
# 		email
# 		city
# 		pincode
# 		address
# 		password
# 		status
# 		state_id
