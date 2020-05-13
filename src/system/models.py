from django.db import models
import secrets
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.core import validators
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)


def upload_to_user(instance, filename):
	name = instance.full_name.replace(' ','_')
	*filenames, ext = filename.split('.')
	a = secrets.token_urlsafe(32)
	return f"User_Profile/{name}_SKY_{a}.{ext}"

def upload_to_book(instance, filename):
	name = instance.name.replace(' ','_')
	*filenames, ext = filename.split('.')
	a = secrets.token_urlsafe(32)
	return f"Book_cover/{name}_SKY_{a}.{ext}"

class MyUserManager(BaseUserManager):
	def create_user(self, full_name, email, contactNo, date_of_birth, state, city, pincode,full_address, profile, password=None):
		if not email:
			raise ValueError('User must have an email address')
		user = self.model(
			full_name=full_name,
			email=self.normalize_email(email),
			date_of_birth=date_of_birth,
			contactNo=contactNo,
			state=state,
			city=city,
			pincode=pincode,
			full_address=full_address,
			profile=profile,
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name=None, contactNo=None, date_of_birth=None, state=None, city=None, pincode=None, full_address=None, profile=None, password=None):
		user = self.create_user(
			full_name=full_name, 
			email=email, 
			contactNo=contactNo, 
			date_of_birth=date_of_birth, 
			state=state, 
			city=city, 
			pincode=pincode,
			full_address=full_address, 
			profile=profile, 
			password=password,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user




class MyUser(AbstractBaseUser):
	state_all = [
		(None, "Select State"),
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
	full_name = models.CharField(
		verbose_name="Full Name",
		max_length=50,
		validators=[
				validators.RegexValidator(regex=r"[A-Za-z]*\s[A-Za-z]*\s[A-Za-z]*", message="Enter Valid Full Name Ex.shyam kumar yadav")],
		# blank=True, #uncomment for super user creation do on all model
		null=True,
	)
	email = models.EmailField(
		verbose_name='email ',
		max_length=255,
		unique=True,
	)
	date_of_birth = models.DateField(
		verbose_name="Data of Birth",
		# blank=True,
		null=True,
	)
	contactNo = models.CharField(verbose_name="Phone Number",
		max_length=13,
		# blank=True,
		null=True,
		validators=[validators.RegexValidator(regex=r"^[6-9]\d{9}$", message="Enter Valid Phone Number."),]
	)
	state = models.CharField(verbose_name="State", 
		max_length=2, 
		# blank=True,
		null=True,
		choices=state_all,
	)
	city = models.CharField(verbose_name="City", max_length=20,
		# blank=True,
		null=True,
		validators=[validators.RegexValidator(regex=r"^\w[A-Za-z ]+$", message="Enter Valid city.")]
	)
	pincode = models.CharField(verbose_name="Pincode",max_length=6,
		# blank=True,
		null=True,
		validators=[
			validators.RegexValidator(regex=r"^\d{6}$", message="Enter Valid pincode.")]
	)
	full_address = models.TextField(verbose_name="Full Address",
		# blank=True,
		null=True,
		max_length=50,
	)
	profile = models.FileField(upload_to=upload_to_user,
		default='Member_Img/default_user.jpg.',
		blank=True,
		validators=[validators.FileExtensionValidator(allowed_extensions=validators.get_available_image_extensions(), message="Select valid Image.")],
	)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = []
	REQUIRED_FIELDS+=['full_name', 'contactNo', 'date_of_birth', 'state', 'city', 'full_address', 'profile']

	#add +91 on Number Bug #552020

	def __str__(self):
		return f"id :{self.id}, {self.email}"

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
		
	@property
	def get_full_name(self):
		return self.full_name

	@property
	def get_short_name(self):
		return "_".join(self.full_name.split(' ')[::2])

	def send_email(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.email], **kwargs)
		
	@property
	def is_staff(self):
		return self.is_admin

class BookAuthor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	def __str__(self):
		return f"{self.first_name}_{self.last_name}"

class BookPublish(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class Genre(models.Model):
	name = models.IntegerField(verbose_name="Genre Name", choices=[(None,"Select Language")]+settings.BOOK_GENRE)

	def __str__(self):
		return self.get_name_display()

class Book(models.Model):
	bookid = models.CharField(max_length=20, primary_key=True, verbose_name="Book ID")
	name = models.CharField(max_length=120, verbose_name="Book Name")
	genre = models.ManyToManyField(Genre, verbose_name="Genre")
	author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, verbose_name="Author Name")
	publish = models.ForeignKey(BookPublish, on_delete=models.CASCADE, verbose_name="Publisher Name")
	publish_Date = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Publish Date")
	language = models.CharField(max_length=12, verbose_name="Language", choices=[(None,"Select Language")]+settings.LANGUAGES)
	edition = models.CharField(max_length=2, verbose_name="Edition")
	cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Book Cost(per unit)")
	page = models.PositiveIntegerField(verbose_name="Total Page")
	description = models.TextField(verbose_name="Book Description")
	stock = models.PositiveIntegerField(verbose_name="Current Stock")
	today_stock = models.PositiveIntegerField(verbose_name="stock", blank=True)
	rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Rating")
	profile = models.FileField(upload_to=upload_to_book, verbose_name="Book cover",
		default="Book_Img/default.png",blank=True,
		validators=[validators.FileExtensionValidator(allowed_extensions=validators.get_available_image_extensions(), message="Select valid Cover.")],
	)
	class Meta:
		ordering = ["name"]

	def save(self, *args, **kwargs):
		self.today_stock = self.stock - self.issue_set.all().count()
		super().save(self, *args, **kwargs)
		if self.profile:
				
			img = Image.open(self.profile.path)
			if img.height > 300 or img.width > 300:
				output_size = (300, 300)
				img.thumbnail(output_size)
				img.save(self.profile.path)
	
	def delete(self, *args, **kwargs):
		self.profile.delete()
		super(Book, self).delete(*args, **kwargs)

	def __str__(self):
		return f"{self.bookid}, {self.name}"

	def display_genre(self):
		return ', '.join(genre.get_name_display() for genre in self.genre.all())
	display_genre.short_description = 'Genre'

	@property
	def get_book_name(self):
		return f"{self.name.replace(' ','_')}"

	def get_absolute_url(self):
		return f'/book/{str(self.bookid)}/{self.author.__str__()}/{self.publish.__str__()}/'

class Issue(models.Model):
	member = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)
	due_date = models.DateField()

	def __str__(self):
		return f"{self.book.get_book_name}@{self.member.get_short_name}"
	
	def save(self, *args, **kwargs):
		print("my save")
		super().save(*args, **kwargs)

