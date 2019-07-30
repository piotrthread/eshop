from django.db import models


VAT_CHOICES = (
    (0.23, "23%"),
    (0.08, "8%"),
    (0.05, "5%"),
    (0, "0%"),
)

class Category(models.Model):
    category_name = models.CharField(max_length = 64)
    slug = models.CharField(max_length = 64, unique = True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length = 128)
    description = models.TextField()
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    vat = models.FloatField(choices = VAT_CHOICES, default = 0.23)
    stock = models.IntegerField()
    categories = models.ManyToManyField(Category)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
