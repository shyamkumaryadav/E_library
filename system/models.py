from django.db import models


class State(models.Model):
	state_id = models.CharField(max_length=2, primary_key=True)
	name = models.CharField(max_length=120)
	def __str__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=120)
	state_id = models.ForeignKey(State, on_delete=models.CASCADE)
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
	state = models.ForeignKey(State, verbose_name='State', on_delete=models.CASCADE)
	city = models.ForeignKey(City, verbose_name='City', on_delete=models.CASCADE)
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


class Test(models.Model):
	F_MEDIA_CHOICES = [
		(None, 'Select Media'),
		('vinyl', 'Vinyl'),
		('cd', 'CD'),
		('vhs', 'VHS Tape'),
		('dvd', 'DVD'),
	]
	MEDIA_CHOICES = [
		(None, 'Select Media'),
		('Audio', (
			('vinyl', 'Vinyl'),
			('cd', 'CD'),
			)
		),
		('Video', (
			('vhs', 'VHS Tape'),
			('dvd', 'DVD'),
			)
		),
		
	]
	f_name =  models.CharField(max_length=120, choices=F_MEDIA_CHOICES, blank=True)
	name = models.CharField(max_length=120, choices=MEDIA_CHOICES, blank=True)
	