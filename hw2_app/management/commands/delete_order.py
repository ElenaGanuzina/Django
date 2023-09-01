from django.core.management.base import BaseCommand
from hw2_app.models import Order


class Command(BaseCommand):
    help = "Delete an order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order id')

    def handle(self, *args, **kwargs):
        order = Order.objects.filter(pk=kwargs.get('pk')).first()
        if order is not None:
            order.delete()
