from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    second_image = models.ImageField(upload_to="products/", blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name