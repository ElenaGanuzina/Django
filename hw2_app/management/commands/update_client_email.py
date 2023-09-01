from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Update a client.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')
        parser.add_argument('email', type=str, help='New email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        email = kwargs.get('email')
        client = Client.objects.filter(pk=pk).first()
        client.email = email
        client.save()
        self.stdout.write(f'{client}')
