from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=10)
    avenue = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    contact_no = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
