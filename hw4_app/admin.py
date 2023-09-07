from django.contrib import admin
from hw2_app.models import Client, Product, Order


@admin.action(description='Drop to zero')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_date']
    ordering = ['registration_date']
    search_fields = ['name']
    search_help_text = 'Search by name'
    readonly_fields = ['name', 'registration_date']
    fields = ['name', 'registration_date', 'email']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'price', 'image']
    search_fields = ['prod_name']
    search_help_text = 'Search by product name'
    readonly_fields = ['prod_name']
    fields = ['prod_name', 'description', 'price', 'quantity', 'add_date', 'image']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'total']
    search_fields = ['order_date']
    search_help_text = 'Search by order date'
    readonly_fields = ['total', 'client']
    fields = ['total', 'order_date', 'client']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
