from django.shortcuts import render

from categories.models import Category


def category(request):
    # import ipdb; ipdb.set_trace()
    category_list = Category.objects.all()
    return render(request, 'home/index.html', {'category_list': category_list})
