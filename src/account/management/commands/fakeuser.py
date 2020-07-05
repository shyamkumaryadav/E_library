from django.core.management.base import BaseCommand, CommandError
import faker
import tqdm
from account.models import User
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests



class Command(BaseCommand):
    help = 'This Make fake User for you...'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int,
                            help='A Number for Data fake.', default=1)
        parser.add_argument('URL', type=str,
                            help='Profile Image url.')

    def handle(self, *args, **kwargs):
        if kwargs['n']:
            for _ in tqdm.tqdm(range(kwargs['n']), desc='Users Created', unit='loop'):
                # try:
                f = faker.Faker()
                username=f.user_name()
                password=f.password()
                u = User(username=username, email=f.email(),
                    first_name=f.first_name(),
                    last_name=f.last_name(),
                    password=password
                )
                u.save()
                url = kwargs['URL']
                print(f"Username: {username}    Password: {password}")
                if url is not None:
                    with NamedTemporaryFile() as temp:
                        temp.name += '.'+ url.split('.')[-1]
                        temp.write(requests.get(url).content)
                        temp.flush()
                        u.profile.save(temp.name, File(temp))

                # except Exception as e:
                #     kwargs['n'] -= 1
                #     continue
        self.stdout.write(self.style.SUCCESS(
            f'{kwargs["n"]} Fake Users is Created...'))