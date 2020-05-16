import secrets
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.core import validators
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


def upload_to_user(instance, filename):
    name = instance.full_name.replace(' ', '_')
    *filenames, ext = filename.split('.')
    a = secrets.token_urlsafe(32)
    return f"User_Profile/{name}_SKY_{a}.{ext}"


class UserManager(BaseUserManager):
    def create_user(self, full_name, email, contactNo, date_of_birth, state, city, pincode, full_address, profile, is_defaulter=False, password=None):
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
            is_defaulter=is_defaulter,
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
        user.is_defaulter = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(
        verbose_name="Full Name",
        max_length=50,
        validators=[
            validators.RegexValidator(regex=r"[A-Za-z]*\s[A-Za-z]*\s[A-Za-z]*", message="Enter Valid Full Name Ex.shyam kumar yadav")],
        null=True,
    )
    email = models.EmailField(
        verbose_name='email ',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(
        verbose_name="Data of Birth",
        null=True,
    )
    contactNo = models.CharField(verbose_name="Phone Number",
                                 max_length=13,
                                 null=True,
                                 validators=[validators.RegexValidator(
                                     regex=r"^[6-9]\d{9}$", message="Enter Valid Phone Number."), ]
                                 )
    state = models.CharField(verbose_name="State",
                             max_length=2,
                             null=True,
                             choices=[(None, "Select State")] +
                             settings.LIST_STATE,
                             )
    city = models.CharField(verbose_name="City", max_length=20,
                            null=True,
                            validators=[validators.RegexValidator(
                                regex=r"^\w[A-Za-z ]+$", message="Enter Valid city.")]
                            )
    pincode = models.CharField(verbose_name="Pincode", max_length=6,
                               null=True,
                               validators=[
                                   validators.RegexValidator(regex=r"^\d{6}$", message="Enter Valid pincode.")]
                               )
    full_address = models.TextField(verbose_name="Full Address",
                                    null=True,
                                    max_length=50,
                                    )
    profile = models.FileField(upload_to=upload_to_user,
                               default='Member_Img/default_user.jpg',
                               blank=True,
                               validators=[validators.FileExtensionValidator(
                                   allowed_extensions=validators.get_available_image_extensions(), message="Select valid Image.")],
                               )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_defaulter = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    REQUIRED_FIELDS += ['full_name', 'contactNo',
                        'date_of_birth', 'state', 'city', 'full_address', 'profile']

    def __str__(self):
        return f"id :{self.id}, {self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def send_email(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def get_full_name(self):
        return self.full_name

    @property
    def get_short_name(self):
        return "_".join(self.full_name.split(' ')[::2])

    @property
    def defaulter(self):
        return self.is_defaulter

    @property
    def get_book_list(self):
        return self.full_name

    @property
    def is_staff(self):
        return self.is_admin
