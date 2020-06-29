import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
)
from otp_twilio.models import TwilioSMSDevice

def upload_to_user(instance, filename):
    name = instance.get_full_name.replace(' ', '_')
    *_, ext = filename.split('.')
    _ = uuid.uuid4
    return f"User_Profile/{name}-SKY-{_}.{ext}"



class AbstractUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        verbose_name="First Name",
        max_length=50,
        validators=[
            validators.RegexValidator(regex=r"^[A-Za-z ]+$", message="Enter Valid Name.")],
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
                                     regex=r"^[4-9]\d{9}$", message="Enter Valid Phone Number."), ]
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
                               help_text= 'Only Image [png, jpe, jpg, jpeg]',
                               validators=[validators.FileExtensionValidator(
                                   allowed_extensions=validators.get_available_image_extensions(),
                                   message="'%(extension)s' not valid Profile Image."
                                   )
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
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'