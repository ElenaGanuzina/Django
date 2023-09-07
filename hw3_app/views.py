from datetime import timedelta, datetime
from django.shortcuts import render
from hw2_app.models import Order


def index(request):
    return render(request, 'hw3_app/base.html')


def get_products_by_period(request, client_id: int, period):
    global start_date
    heading = 'Products ordered during last '
    if period == 'week':
        heading = heading + '7 days'
        start_date = datetime.now() - timedelta(days=7)
    elif period == 'month':
        heading = heading + '30 days'
        start_date = datetime.now() - timedelta(days=30)
    elif period == 'year':
        heading = heading + '365 days'
        start_date = datetime.now() - timedelta(days=365)

    ordered_products = set()
    orders = Order.objects.filter(client__pk=client_id,
                                  order_date__range=[start_date, datetime.now()])
    for order in orders:
        ordered_products.update(product for product in order.products.all())
    return render(request, 'hw3_app/ordered_products.html',
                  {'ordered_products': ordered_products, 'heading': heading})
