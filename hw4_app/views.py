from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm
from hw2_app.models import Product


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            prod_name = form.cleaned_data['prod_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            product = Product(prod_name=prod_name, description=description, price=price, quantity=quantity, image=image)
            product.save()
            return HttpResponse('<h3>Product was successfully uploaded</h3>')
    else:
        form = ProductForm()
    return render(request, 'hw4_app/upload_product.html', {'form': form})



