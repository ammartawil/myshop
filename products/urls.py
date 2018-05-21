# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf.urls import url, include

from products import views


urlpatterns = [
    url(r'^(?P<product_slug>[\w-]+)$', views.product_view, name='view-product'),
]