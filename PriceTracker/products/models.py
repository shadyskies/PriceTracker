from django.db import models


# Create your models here.

class Product(models.Model):
    user_id = models.IntegerField()
    links = models.TextField(blank=True, null=True)
