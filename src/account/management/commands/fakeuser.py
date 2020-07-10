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
                users = []
                passwd = []
                try:
                    f = faker.Faker(['en_US', 'hi_IN'])
                    username = f.user_name()
                    password = f.password()
                    u = User(username=username, email=f.email(),
                             first_name=f.first_name(),
                             last_name=f.last_name(),
                             date_of_birth=f.date_of_birth(),
                             state=f.random_element([i[0] for i in User.state.field.choices[1:]]),
                             city=f.city(),
                             pincode=f.postcode(),
                            full_address=f.address(),
                             )
                    u.set_password(password)
                    u.save()
                    u.profile.save(f'{uuid.uuid4()}.jpg', ContentFile(
                        requests.get('https://picsum.photos/300').content))
                    users.append(username)
                    passwd.append(password)

                except Exception as e:
                    kwargs['n'] -= 1
        Users = {str(i):{'username':users[i], 'password':passwd[i]} for i in range(len(users))}
        self.stdout.write(self.style.SUCCESS(
            f'{kwargs["n"]} Fake Users is Created...'))
        for key in Users:
            self.stdout.write(self.style.SUCCESS(f'{Users[key]}'))
