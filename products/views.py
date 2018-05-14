from django.shortcuts import render

from products.models import Product


def product_view(request, product):
    product_details = Product.objects.get(slug=product)
    return render(request, 'product/product.html', {'product': product_details})
