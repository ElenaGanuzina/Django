from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = 'Update product price.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')
        parser.add_argument('price', type=float, help='New price')

    def handle(self, *args, **kwargs):
        product = Product.objects.filter(pk=kwargs.get('pk')).first()
        product.price = kwargs.get('price')
        product.save()
        self.stdout.write(f'{product}')