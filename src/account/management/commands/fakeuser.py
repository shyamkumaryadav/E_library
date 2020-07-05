from django.core.management.base import BaseCommand, CommandError
import faker
import tqdm
import requests
import uuid
from account.models import User
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'This Make fake User for you...'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int,
                            help='A Number for Data fake.', default=1)

    def handle(self, *args, **kwargs):
        if kwargs['n']:
            for _ in tqdm.tqdm(range(kwargs['n']), desc='Users Created', unit='loop'):
                try:
                    f = faker.Faker()
                    username = f.user_name()
                    password = f.password()
                    u = User(username=username, email=f.email(),
                             first_name=f.first_name(),
                             last_name=f.last_name(),
                             password=password
                             )
                    u.save()
                    print(f"Username: {username}    Password: {password}")
                    u.profile.save(f'{uuid.uuid4()}.jpg', ContentFile(
                        requests.get('https://picsum.photos/300').content))

                except Exception as e:
                    kwargs['n'] -= 1
                    continue
        self.stdout.write(self.style.SUCCESS(
            f'{kwargs["n"]} Fake Users is Created...'))
