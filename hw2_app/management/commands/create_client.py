from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Create a client."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, nargs='*', help='Client name')
        parser.add_argument('email', type=str, help="Client email")
        parser.add_argument('phone', type=str, help="Client email")
        parser.add_argument('address', type=str, nargs='*', help="Client email")

    def handle(self, *args, **kwargs):
        client = Client(name=kwargs.get('name'), email=kwargs.get('email'),
                        phone=kwargs.get('phone'), address=' '.join(kwargs.get('address')))
        client.save()
        self.stdout.write(f'{client}')

