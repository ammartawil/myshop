from django.shortcuts import render

from categories.models import Category
# Create your views here.


def homepage(request):
    category_list = Category.objects.filter(main_category=True)
    return render(request, 'home/index.html', {'category_list': category_list})
