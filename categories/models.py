from django.db import models


class Size(models.Model):
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
    )
    uk_size = models.CharField(max_length=4)


class Category(models.Model):
    name = models.CharField(max_length=60)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
    )
