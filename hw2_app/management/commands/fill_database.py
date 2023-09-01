from django.core.management.base import BaseCommand
from hw2_app.models import Client, Product, Order
from random import randint, uniform, choices


class Command(BaseCommand):
    help = 'Fill database with fake data.'

    def handle(self, *args, **options):
        clients = []
        for i in range(10):
            client = Client(name=f'Client{i}', email=f'client{i}@mail.com',
                            address=f'Fake address {i}', phone=f'{randint(10000000, 100000000)}')
            client.save()
            clients.append(client)

        products = []
        for i in range(10):
            product = Product(prod_name=f'Product{i}', description=f'Product{i} description',
                              price=round(uniform(1, 5000), 2), quantity=randint(1, 200))
            product.save()
            products.append(product)

        for client in clients:
            ordered_products = choices(products, k=3)
            total = 0
            for product in products:
                total += product.price
            order = Order(client=client, total=total)
            order.save()
            order.products.set(ordered_products)

