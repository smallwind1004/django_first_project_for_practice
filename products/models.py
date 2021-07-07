from django.db import models

# Create your models here.
class Products(models.Model):
    title       = models.CharField(max_length=120)
    discription = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField(blank=True, null=False)
    featured    = models.BooleanField(default=True)