from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:client_id>/<slug:period>', views.get_products_by_period, name='get_products_by_period'),
]
