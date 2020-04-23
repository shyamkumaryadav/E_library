from django.db import models


states = [
	('AP', 'Andhra Pradesh'),
	('AR', 'Arunachal Pradesh'),
	('AS', 'Assam'),
	('BR', 'Bihar'),
	('CT', 'Chhattisgarh'),
	('GA', 'Goa'),
	('GJ', 'Gujarat'),
	('HR', 'Haryana'),
	('HP', 'Himachal Pradesh'),
	('JH', 'Jharkhand'),
	('KA', 'Karnataka'),
	('KL', 'Kerala'),
	('MP', 'Madhya Pradesh'),
	('MH', 'Maharashtra'),
	('MN', 'Manipur'),
	('ML', 'Meghalaya'),
	('MZ', 'Mizoram'),
	('NL', 'Nagaland'),
	('OR', 'Odisha'),
	('PB', 'Punjab'),
	('RJ', 'Rajasthan'),
	('SK', 'Sikkim'),
	('TN', 'Tamil Nadu'),
	('TG', 'Telangana'),
	('TR', 'Tripura'),
	('UT', 'Uttarakhand'),
	('UP', 'Uttar Pradesh'),
	('WB', 'West Bengal'),
	('AN', 'Andaman and Nicobar Islands'),
	('CH', 'Chandigarh'),
	('DB', 'Dadra and Nagar Haveli'),
	('DD', 'Daman and Diu'),
	('DL', 'Delhi'),
	('JK', 'Jammu and Kashmir'),
	('LA', 'Ladakh'),
	('LD', 'Lakshadweep'),
	('PY', 'Puducherry'),
]
'''
To Run 
for i in range(len(states)):
	State(id=i+1, name=states[i][1]).save()
'''

citys = [
	(None, 'choice City'),
	('Andhra Pradesh', (
			('mp', 'Madesdsds'),
		)),
	('Arunachal Pradesh', (
			('as', 'asasasasa'),
		)),
	
]

# Mumbai	1,756
# Pune	351
# Thane	270
# Nashik	46
# Nagpur	44
# Palghar	34
# Ahmadnagar	27
# Sangli	26
# Aurangabad	23
# Buldana	17
# Raigarh	15
# Akola	12
# Other States*	11
# Latur	8
# Satara	6
# Ratnagiri	6
# Kolhapur	6
# Amravati	6
# Yavatmal	5
# Osmanabad	4
# Jalgaon	2
# Dhule	2
# Washim	1
# Solapur	1
# Sindhudurg	1
# Jalna	1
# Hingoli	1
# Gondiya	1
# Bid
class State(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=120)
	def __str__(self):
		return self.name


class BookAuthor(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')
	name = models.CharField(max_length=120, verbose_name='Author Name')

	def __str__(self):
		return self.name

class BookPublish(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True, verbose_name='ID')
	name = models.CharField(max_length=120, verbose_name='Publisher Name')

	def __str__(self):
		return self.name

class Book(models.Model):
	bookid = models.CharField(max_length=20, primary_key=True, verbose_name='Book ID')
	name = models.CharField(max_length=120, verbose_name='Name')
	genre = models.CharField(max_length=2, verbose_name='Genre')
	author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE)
	publish = models.ForeignKey(BookPublish, on_delete=models.CASCADE)
	publish_Date = models.DateField(auto_now=False, auto_now_add=True)
	language = models.CharField(max_length=2)
	edition = models.CharField(max_length=2)
	cost = models.DecimalField(max_digits=8, decimal_places=2)
	page = models.PositiveIntegerField()
	description = models.TextField()
	stock = models.PositiveIntegerField()
	today_stock = models.PositiveIntegerField()
	rating = models.DecimalField(max_digits=3, decimal_places=1)
	profile = models.FileField(upload_to='')



	def __str__(self):
		return self.name

class Member(models.Model):
	name = models.CharField(max_length=120, verbose_name='Full Name')
	username = models.CharField(max_length=120,verbose_name='Username')
	birthday = models.DateField(verbose_name='Date of Birth')
	phone = models.PositiveIntegerField(verbose_name=' Contact No')
	email = models.EmailField(verbose_name='Email ID')
	# state = models.ForeignKey(State, on_delete=models.CASCADE)
	state = models.CharField(max_length=2,verbose_name='State', choices=states)
	city = models.CharField(max_length=102, verbose_name='City')
	pincode = models.CharField(max_length=102, verbose_name='Pincode')
	address = models.CharField(max_length=102, verbose_name='Full Address')
	password = models.CharField(max_length=102, verbose_name='Password')
	status = models.BooleanField(default=False, verbose_name='Account Status')
	#profile = models.FileField(upload_to=/media/)

	def __str__(self):
		return self.username


class Issue(models.Model):
	member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	date=models.DateField(verbose_name='Date')
	due_date = models.DateField()


