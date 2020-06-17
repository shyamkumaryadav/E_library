from django.core.management.base import BaseCommand, CommandError
import faker
import tqdm
from django.conf import settings
from system.models import Book, BookAuthor, BookPublish, Genre


class Command(BaseCommand):
    help = 'This Make fake data for you...'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int,
                            help='A Number for Data fake.', default=1)

    def handle(self, *args, **kwargs):
        try:
            if kwargs['n'] > 1:
                for _ in tqdm.tqdm(range(kwargs['n'])):
                    AddBook()
            else:
                AddBook()
            self.stdout.write(self.style.SUCCESS(
                f'{kwargs["n"]} Data fake is Created...'))
        except:
            raise CommandError('something is Wrong.')


lg = [settings.LANGUAGES[i][0] for i in range(len(settings.LANGUAGES))]
be = [settings.BOOK_EDITION[i][0] for i in range(len(settings.BOOK_EDITION))]
bg = [settings.BOOK_GENRE[i][0] for i in range(len(settings.BOOK_GENRE))]

f = faker.Faker()


def AddBook():
    publish, _ = BookPublish.objects.get_or_create(
        name=f.company(), address=f.address())
    author, _ = BookAuthor.objects.get_or_create(
        first_name=f.first_name(),
        last_name=f.last_name(),
        date_of_birth=f.date_of_birth(),
        date_of_death=f.date_this_year()
    )
    genre = Genre.objects.filter(
        name__in=f.random_elements(
            bg, length=f.random_int(
                min=1, max=6),
            unique=True)
    )
    book, _ = Book.objects.get_or_create(
        name=f.name(),
        author=author,
        publish=publish,
        publish_date=f.date(),
        language=f.random_element(lg),
        edition=f.random_element(be),
        cost=f.pydecimal(
            right_digits=2, positive=True, min_value=100, max_value=9999
        ),
        page=f.pyint(),
        description=f.catch_phrase(),
        stock=f.pyint(),
        rating=f.pydecimal(right_digits=1, positive=True,
                           min_value=0, max_value=10),
    )
    book.genre.set([*genre])
    book.save()
