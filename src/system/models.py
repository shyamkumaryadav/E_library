import secrets
import uuid
from django.db import models
from django.conf import settings
from django.core import validators
from django.urls import reverse_lazy
from PIL import Image
from account.models import User


def upload_to_book(instance, filename):
    print(dir(instance))
    print(dir(filename))
    # instance.profile.delete()
    name = instance.name.replace(' ', '_')
    *_, ext = filename.split('.')
    a = secrets.token_urlsafe(32)
    return f"Book_cover/{name}_SKY_{a}.{ext}"


class BookAuthor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(
        verbose_name='Death Date', null=True, blank=True)

    class Meta:
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_update_url(self):
        return reverse_lazy('system:authormanagementupdate', kwargs={
            'pk': self.pk
        })


class BookPublish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True,
                            error_messages={
                                "unique": "The name is already exists."
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


class Genre(models.Model):
    name = models.IntegerField(verbose_name="Genre Name", choices=[
                               (None, "Select Language")] + settings.BOOK_GENRE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.get_name_display())


class Book(models.Model):
    id = models.UUIDField(verbose_name="Book ID",
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name="Book Name")
    genre = models.ManyToManyField(Genre, verbose_name="Genre")
    author = models.ForeignKey(
        BookAuthor, on_delete=models.CASCADE, verbose_name="Author Name")
    publish = models.ForeignKey('BookPublish', on_delete=models.CASCADE, to_field='address',
                                verbose_name="Publisher Name")
    # publish.empty_values = ['adres']
    # print('*'*13)
    # print(publish.get_choices.__dir__()
    publish_date = models.DateField(verbose_name="Publish Date")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")
    language = models.CharField(max_length=12, verbose_name="Language", choices=[
                                (None, "Select Language")] + settings.LANGUAGES)
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
        max_digits=3, decimal_places=1, verbose_name="Rating")
    profile = models.FileField(
        upload_to=upload_to_book, verbose_name="Book cover",
        default="Book_cover/default.png", blank=True,
        validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Cover Image.")
        ],
    )

    class Meta:
        ordering = ['-publish_date']

    def delete(self, *args, **kwargs):
        self.profile.delete()
        super(Book, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def list_genre(self):
        return ', '.join(genre.get_name_display() for genre in self.genre.all())

    def display_genre(self):
        return ', '.join(genre.get_name_display() for genre in self.genre.all())
    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        # return f'/book/{str(self.bookid)}/'
        pass


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
