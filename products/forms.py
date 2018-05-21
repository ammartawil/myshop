# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from django import forms

from categories.models import Size
from .models import Colour



class ProductForm(forms.Form):
    def __init__(self,product_slug):
        super(ProductForm, self).__init__()
        self.fields['available_colours'].queryset = Colour.objects.filter(product__slug=product_slug)
        self.fields['available_sizes'].queryset = Size.objects.filter(product__slug=product_slug)

    available_colours = forms.ModelChoiceField(
        label='Available colours',
        queryset=None
    )

    available_sizes = forms.ModelChoiceField(
        label='Available sizes',
        queryset=None
    )

    quantity = forms.DecimalField(decimal_places=0)
