from django.db import models


states = [
	(None, 'choice State'),
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

city = [
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

class BookAuthor(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')
	name = models.CharField(max_length=120, verbose_name='Name')

	def __str__(self):
		return self.name

class BookPublish(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True, verbose_name='ID')
	name = models.CharField(max_length=120, verbose_name='Name')

	def __str__(self):
		return self.name

class Book(models.Model):
	bookid = models.AutoField(primary_key=True,auto_created=True, verbose_name='ID')
	name = models.CharField(max_length=120, verbose_name='Name')

	def __str__(self):
		return self.name

class Issue(models.Model):
	date=models.CharField(max_length=120, verbose_name='Date')

	def __str__(self):
		return self.date

class Test(models.Model):
	state=models.CharField(max_length=2, choices=states)
	city=models.CharField(max_length=2, choices=city)


	def __str__(self):
		return self.state
