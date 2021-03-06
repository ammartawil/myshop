from django.db import models

from categories.models import Category, Size


class Colour(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    colour = models.ManyToManyField(Colour)
    category = models.ForeignKey(Category)
    sizes_available = models.ManyToManyField(Size)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
