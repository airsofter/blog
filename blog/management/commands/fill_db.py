import json
import os

from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from blog.models import Post


def load_from_json(file_name: str) -> dict:
    with open(
            os.path.join(settings.JSON_PATH, f'{file_name}.json'),
            encoding='utf-8'
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        self.create_users()
        self.create_posts()

    def create_users(self):
        self.migrate()
        try:
            if not get_user_model().objects.exists():
                self.migrate()
                get_user_model().objects.create_superuser(
                    username='skywalker_89',
                    email='skywalker_89@example.com',
                    password='R3b3lAlliance!')

                get_user_model().objects.create_user(
                    username='silverdragon23',
                    email='silverdragon23@mail.com',
                    password='Dr@gonFire987')

                get_user_model().objects.create_user(
                    username='mystic_galaxy',
                    email='mystic_galaxy55@gmail.com',
                    password='Starlight#2024')

                self.syncdb()
        except Exception as e:
            print(e)
            self.create_users()

    def create_posts(self):
        posts = load_from_json('blogapp_post')
        if not Post.objects.exists():
            Post.objects.all().delete()
            for post in posts:
                user_name = post['fields']['user']
                _user = get_user_model().objects.get(id=user_name)
                post['fields']['user'] = _user

                new_publication = Post(**{'id': post['pk']},
                                           **post['fields'])
                new_publication.save()

            self.reset_sequences()
            self.collect_static()

    @staticmethod
    def migrate():
        os.system('python manage.py migrate --noinput')

    @staticmethod
    def syncdb():
        os.system('python manage.py migrate --run-syncdb')

    @staticmethod
    def reset_sequences():
        sequence_sql = connection.ops.sequence_reset_sql(
            no_style(), [Post, get_user_model()])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

    @staticmethod
    def collect_static():
        os.system('python manage.py collectstatic --no-input --clear')
