from django.db import models
from store.models import Store

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand)
    unit = models.ForeignKey(Unit)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

class StoreCatalog(models.Model):
    product = models.ForeignKey(Product)
    store = models.ManyToManyField(Store)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return "%s is available in %s" % (self.product, self.store)
