import uuid
import secrets
from django.db import models
from system import data_list
from django.utils import timezone
from django.core import validators
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager, AbstractUser as BaseAbstractUser
)
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return f"elibrary{secrets.token_hex()}.{filename.split('.')[-1]}"


def profile_size(value):
    if value.size > 1024 * 1024 * 0.5:
        raise ValidationError(f"Image size is {filesizeformat(value.size)} required size {filesizeformat(1024 * 1024 * 0.5)}")

def age_18(value, message="You sude be 18+"):
    aaj = value.today()
    age = aaj.year - value.year - \
        ((aaj.month, aaj.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(message)


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
    
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=30,
        unique=True,
    )
    date_of_birth = models.DateField(
        verbose_name=_("Data of Birth"),
        null=True,
        validators=[age_18]
    )
    phone_number = models.CharField(verbose_name=_("Phone Number"),
                                    max_length=13,
                                    null=True,
                                    validators=[validators.RegexValidator(
                                        regex=r"^[4-9]\d{9}$", message=_("Enter Valid Phone Number.")), ]
                                    )
    state = models.CharField(verbose_name=_("State"),
                             max_length=2,
                             null=True,
                             choices=[(None, _("Select State"))] +
                             data_list.LIST_STATE,
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
    is_defaulter = models.BooleanField(
        _('defaulter'),
        default=False,
        help_text=_(
            'User in defaulter list or not?'
        ),
    )
    profile = models.FileField(upload_to=upload_to,
                               default='default.jpg', blank=True,
                               help_text=_(
                                   'Only Image (png, jpe, jpg, jpeg) extensions'),
                               validators=[validators.FileExtensionValidator(
                                   allowed_extensions=validators.get_available_image_extensions(),
                                   message=_(
                                       "'%(extension)s' not valid Profile Image.")
                               ), profile_size
                               ],)
    class Meta(BaseAbstractUser.Meta):
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    @property
    def get_update_url(self):
        return reverse_lazy('account:update', kwargs={
            'username': self.username
        })

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
        ordering = ['username']
