from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

