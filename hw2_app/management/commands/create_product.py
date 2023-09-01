from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Create a product."

    def add_arguments(self, parser):
        parser.add_argument('prod_name', type=str, nargs='*', help='Product name')
        parser.add_argument('description', type=str, nargs='*', help="Product description")
        parser.add_argument('price', type=float, help="Product price")
        parser.add_argument('quantity', type=int, help="Product quantity")

    def handle(self, *args, **options):
        product = Product(prod_name=' '.join(options['prod_name']),
                          description=' '.join(options['description']),
                          price=options['price'], quantity=options['quantity'])
        product.save()
