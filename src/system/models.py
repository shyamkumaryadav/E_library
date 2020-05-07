from django.db import models
import hashlib
from django.core import validators
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

def upload_to_sky(instance, filename):
	name = instance.full_name.replace(' ','_')
	*filenames, ext = filename.split('.')
	a = hashlib.sha224(b'{name}').hexdigest()
	return f"Member_Img/{a[::-1]}{a}.{extention}"

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
	profile = models.FileField(upload_to=upload_to_sky,
		default='Member_Img/default_user.jpg.',
		blank=True,
	)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	REQUIRED_FIELDS+=['full_name', 'contactNo', 'date_of_birth', 'state', 'city', 'full_address', 'profile']

	#add +91 on Number Bug #552020

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

class BookAuthor(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class BookPublish(models.Model):
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

class Issue(models.Model):
	member_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	date=models.DateField()
	due_date = models.DateField()

# 4006056 40223  5 55 1212 12 45  12 12 45 4545454545 123456