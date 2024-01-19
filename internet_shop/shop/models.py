from django.db import models


# Create your models here.

class Cotegory(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    cotegory = models.ForeignKey(Cotegory,on_delete=models.CASCADE)

