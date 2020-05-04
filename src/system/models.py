from django.db import models


class BookAuthor(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True, serialize=False)
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class BookPublish(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True)
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class Book(models.Model):
	bookid = models.CharField(max_length=20, primary_key=True)
	name = models.CharField(max_length=120)
	genre = models.CharField(max_length=2)
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
	profile = models.FileField(upload_to='Book_Img/')

	def __str__(self):
		return self.name

class Member(models.Model):
	pass

class Issue(models.Model):
	# member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	date=models.DateField()
	due_date = models.DateField()
