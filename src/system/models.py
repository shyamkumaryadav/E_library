import secrets
from django.db import models
from django.conf import settings
from django.core import validators
from PIL import Image
from account.models import User


def upload_to_book(instance, filename):
    name = instance.name.replace(' ', '_')
    *filenames, ext = filename.split('.')
    a = secrets.token_urlsafe(32)
    return f"Book_cover/{name}_SKY_{a}.{ext}"


class BookAuthor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(
        verbose_name='Died', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookPublish(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.IntegerField(verbose_name="Genre Name", choices=[
                               (None, "Select Language")] + settings.BOOK_GENRE)

    def __str__(self):
        return self.get_name_display()


class Book(models.Model):
    bookid = models.CharField(
        max_length=120, primary_key=True, verbose_name="Book ID")
    name = models.CharField(max_length=120, verbose_name="Book Name")
    genre = models.ManyToManyField(Genre, verbose_name="Genre")
    author = models.ForeignKey(
        BookAuthor, on_delete=models.CASCADE, verbose_name="Author Name")
    publish = models.ForeignKey(BookPublish, on_delete=models.CASCADE,
                                verbose_name="Publisher Name")
    publish_Date = models.DateField(
        auto_now=False, auto_now_add=True, verbose_name="Publish Date")
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
        ordering = ["bookid"]

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

    # def get_absolute_url(self):
    #     return f'/book/{str(self.bookid)}/{self.author.__str__()}/\
    # {self.publish.__str__()}/'


class Issue(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.book.get_book_name}@{self.member.get_short_name}"

    # def save(self, *args, **kwargs):
    #   print("my save")
    #   super().save(*args, **kwargs)
