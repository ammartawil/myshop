from django.shortcuts import render, HttpResponseRedirect

from .models import Product
from .forms import ProductForm


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if request.method == 'POST':
        return HttpResponseRedirect('/thanks/')
    else:
        form = ProductForm(product_slug=product_slug)

    return render(request, 'product/product.html', {'product': product, 'form': form})
