from django.contrib import admin

from products.models import Product, Colour


admin.site.register(Colour)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
            'slug': ('name',),
    }


admin.site.register(Product, ProductAdmin)