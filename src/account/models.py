import uuid
import secrets
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager, AbstractUser as BaseAbstractUser
)
from otp_twilio.models import TwilioSMSDevice
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return f"elibrary{secrets.token_hex()}.{filename.split('.')[-1]}"


class AbstractUser(BaseAbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=50,
        validators=[
            validators.RegexValidator(regex=r"^[A-Za-z ]+$", message=_("Enter Valid Name."))],
        null=True,
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"),
        max_length=20,
        validators=[
            validators.RegexValidator(regex=r"^[A-Za-z]+$", message=_("Enter Valid Last Name."))],
        null=True,
    )
    # username = models.CharField(
    #     verbose_name='Username',
    #     max_length=16,
    #     unique=True,
    #     help_text=_('16 characters or fewer. Letters, digits and @ or _ only.'),
    #     validators=[UnicodeUsernameValidator()],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=30,
        unique=True,
    )
    date_of_birth = models.DateField(
        verbose_name=_("Data of Birth"),
        null=True,
    )
    contactNo = models.CharField(verbose_name=_("Phone Number"),
                                 max_length=13,
                                 null=True,
                                 validators=[validators.RegexValidator(
                                     regex=r"^[4-9]\d{9}$", message=_("Enter Valid Phone Number.")), ]
                                 )
    state = models.CharField(verbose_name=_("State"),
                             max_length=2,
                             null=True,
                             choices=[(None, _("Select State"))] +
                             settings.LIST_STATE,
                             )
    city = models.CharField(verbose_name=_("City"), max_length=20,
                            null=True,
                            validators=[validators.RegexValidator(
                                regex=r"^\w[A-Za-z ]+$", message=_("Enter Valid city."))]
                            )
    pincode = models.CharField(verbose_name=_("Pincode"), max_length=6,
                               null=True,
                               )
    full_address = models.TextField(verbose_name=_("Full Address"),
                                    null=True,
                                    max_length=50,
                                    )
    profile = models.FileField(upload_to=upload_to,
                               default='default.jpg', blank=True,
                               help_text=_(
                                   'Only Image (png, jpe, jpg, jpeg) extensions'),
                               validators=[validators.FileExtensionValidator(
                                   allowed_extensions=validators.get_available_image_extensions(),
                                   message=_(
                                       "'%(extension)s' not valid Profile Image.")
                               )
                               ],)
    # is_staff = models.BooleanField(verbose_name=_('staff status'), default=False, help_text=_(
    #     'Designates whether the user can log into this admin site.'))
    # is_active = models.BooleanField(default=True,
    #                                 help_text=_('Designates whether this user should be treated as active. '
    #                                             'Unselect this instead of deleting accounts.'),
    #                                 )
    # is_defaulter = False

    # date_joined = models.DateTimeField(
    #     verbose_name=_('date joined'), default=timezone.now)

    # objects = UserManager()

    # USERNAME_FIELD = 'username'
    # EMAIL_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    class Meta(BaseAbstractUser.Meta):
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)

    # def __str__(self):
    #     return self.username

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    # def get_full_name(self):
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     """Return the short name for the user."""
    #     return self.first_name

    @property
    def prourl(self):
        if self.profile and hasattr(self.profile, 'url'):
            return self.profile.url
        else:
            return "https://picsum.photos/300"


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
