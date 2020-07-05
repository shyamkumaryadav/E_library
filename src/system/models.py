import uuid
import secrets
from django.db import models
from django.utils import timezone
from django.conf import settings, global_settings
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.urls import reverse_lazy
from PIL import Image
from account.models import User, upload_to


@deconstructible
class On_date:
    year = 1
    sign = ''

    def __init__(self, year=None, sign=None):
        if year is not None:
            self.year = year
        if sign is not None:
            self.sign = sign

    def __call__(self, value):
        print('how the valide..')
        if int(value.year) > int(timezone.now().year - self.year):
            raise ValidationError(f'You must be {self.year}{self.sign}')

    def __eq__(self, other):
        return (
            isinstance(other, On_date) and
            (self.year == other.year) and
            (self.sign == other.sign)
        )


class BookAuthor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    date_of_birth = models.DateField(
        null=True, validators=[On_date(year=15, sign='+'), ])
    date_of_death = models.DateField(
        verbose_name='Death Date', null=True, blank=True)

    class Meta:
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean_fields(self, exclude=None):
        if self.date_of_death:
            if self.date_of_birth.year > self.date_of_death.year - 5:
                raise ValidationError({'date_of_death': 'it"s not valid'})

    # def clean(self):
    #     raise ValidationError('this is error')

    @property
    def get_update_url(self):
        return reverse_lazy('system:authormanagementupdate', kwargs={
            'pk': self.pk
        })


class BookPublish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True,
                            error_messages={
                                "unique": "This name is already exists."
                            }
                            )
    address = models.TextField(unique=True,)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def get_update_url(self):
        return reverse_lazy('system:publishermanagementupdate', kwargs={
            'pk': self.pk
        })


class GenreManager(models.Manager):
    def test0001(self):
        n = 0
        for i in settings.BOOK_GENRE:
            obj, _ = self.get_or_create(name=i[0])
            if _:
                n += 1
        return n


class Genre(models.Model):
    name = models.IntegerField(verbose_name="Genre Name", choices=[
                               (None, "Select Language")] + settings.BOOK_GENRE)
    objects = GenreManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.get_name_display())


class Book(models.Model):
    id = models.UUIDField(verbose_name="Book ID",
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name="Name", unique=True)
    genre = models.ManyToManyField(
        Genre, verbose_name="Genre", help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.')
    author = models.ForeignKey(
        BookAuthor, on_delete=models.CASCADE, verbose_name="Author Name")
    publish = models.ForeignKey('BookPublish', on_delete=models.CASCADE,
                                verbose_name="Publisher Name")
    publish_date = models.DateField(
        validators=[On_date, ], verbose_name="Publish Date")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")
    language = models.CharField(max_length=12, verbose_name="Language", choices=[
                                (None, "Select Language")] + global_settings.LANGUAGES)
    edition = models.IntegerField(verbose_name="Edition", choices=[
                                  (None, "Select Edition")] + settings.BOOK_EDITION)
    cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Book Cost(per unit)")
    page = models.PositiveIntegerField(verbose_name="Total Page")
    description = models.TextField(verbose_name="Book Description")
    stock = models.PositiveIntegerField(verbose_name="Stock")
    today_stock = models.PositiveIntegerField(
        verbose_name="Current stock", null=True, blank=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name="Rating")
    profile = models.FileField(
        upload_to=upload_to, verbose_name="Book cover",
        default="default.jpg", blank=True,
        validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Cover Image.")
        ],
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def get_update_url(self):
        return reverse_lazy('system:bookinventoryupdate', kwargs={
            'pk': self.pk
        })


class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={
                             'is_defaulter': False})
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    class Meta:
        unique_together = ('user', 'book',)

    def __str__(self):
        return f"{self.book}, {self.user}"
