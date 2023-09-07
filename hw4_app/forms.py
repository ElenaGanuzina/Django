from django import forms


class ProductForm(forms.Form):
    prod_name = forms.CharField(label='Product name')
    description = forms.CharField(label='Description', max_length=1000, widget=forms.Textarea)
    price = forms.DecimalField(label='Price', max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(label='Quantity')
    image = forms.ImageField(label='Product image')
