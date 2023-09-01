from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = 'Get all the products.'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write(f'{products}')
