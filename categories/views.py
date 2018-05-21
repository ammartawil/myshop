from django.shortcuts import render

from categories.models import Category
from products.models import Product


def category(request, category):
    category_list = Category.objects.filter(parent__name=category)
    product_list = Product.objects.filter(category__slug=category)
    return render(
        request,
        'category/sub_categories.html',
        {'category': category, 'category_list': category_list, 'product_List': product_list}
    )
