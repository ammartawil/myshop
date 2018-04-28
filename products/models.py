from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=60)
    colour = models.ForeignKey(Colours, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes_available = models.ManyToManyField(Sizes)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
