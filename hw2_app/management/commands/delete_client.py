from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Delete a client."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=kwargs['pk']).first()
        if client is not None:
            client.delete()
