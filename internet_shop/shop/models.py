from django.db import models


# Create your models here.

def image_product_path(instance, filename):
    return f"products/{instance.category.name}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    available = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_product_path, blank=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.price} p."

    class Meta:
        ordering = ['name']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукция'
