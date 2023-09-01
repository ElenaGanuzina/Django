from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Delete a product."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product id')

    def handle(self, *args, **kwargs):
        product = Product.objects.filter(pk=kwargs.get('pk')).first()
        if product is not None:
            product.delete()
