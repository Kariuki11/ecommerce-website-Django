from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('IC', 'Icecreams'),
    ('CZ', 'Cheese'),
    ('GH', 'Ghee'),
    ('PN', 'Paneer')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    #selling_price = models.FilteredRelation()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
