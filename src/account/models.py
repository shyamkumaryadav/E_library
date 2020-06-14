import secrets
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
)


def upload_to_user(instance, filename):
    name = instance.get_full_name.replace(' ', '_')
    *filenames, ext = filename.split('.')
    a = secrets.token_urlsafe(32)
    return f"User_Profile/{name}_SKY_{a}.{ext}"


class UserManager123(BaseUserManager):
    def _create_user(self, first_name, last_name, username, email, contactNo, date_of_birth, state, city, pincode, full_address, profile, is_defaulter=False, password=None):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=self.model.normalize_username(username),
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
    def create_user(self, first_name, last_name, username, email, contactNo, date_of_birth, state, city, pincode, full_address, profile, is_defaulter=False, password=None):
        pass

    def create_superuser(self, username, email, first_name=None, last_name=None, contactNo=None, date_of_birth=None, state=None, city=None, pincode=None, full_address=None, profile=None, password=None):
        user = self._create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
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
        user.is_staff = True
        user.is_superuser = True
        if user.is_staff is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if user.is_superuser is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        verbose_name="First Name",
        max_length=50,
        validators=[
            validators.RegexValidator(regex=r"^[A-Za-z ]+$", message="Enter Valid First Name.")],
        null=True,
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=20,
        validators=[
            validators.RegexValidator(regex=r"^[A-Za-z]+$", message="Enter Valid Last Name.")],
        null=True,
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=16,
        unique=True,
        help_text='16 characters or fewer. Letters, digits and @ or _ only.',
        validators=[UnicodeUsernameValidator()],
        # error_messages={
        #     'unique': "A user with that username already exists.", }
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=30,
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
                               default='User_Profile/default.png',
                               validators=[validators.FileExtensionValidator(
                                   allowed_extensions=validators.get_available_image_extensions(),
                                   message="Select valid Profile Image.")
                               ],)
    is_staff = models.BooleanField('staff status', default=False,help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField(default=True,
        help_text='Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.',
        )
    is_defaulter = models.BooleanField(default=False)

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def get_first_name(self):
        return self.first_name
