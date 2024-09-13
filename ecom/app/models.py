from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES = (
    ('Nairobi', 'Nairobi'),
('Mombasa', 'Mombasa'),
('Kisumu', 'Kisumu'),
('Nakuru', 'Nakuru'),
('Kiambu', 'Kiambu'),
('Nyeri', 'Nyeri'),
('Murang’a', 'Murang’a'),
('Kirinyaga', 'Kerugoya'),
('Embu', 'Embu'),
('Machakos', 'Machakos'),
('Kitui', 'Kitui'),
('Makueni', 'Wote'),
('Meru', 'Meru'),
('Tharaka Nithi', 'Chuka'),
('Isiolo', 'Isiolo'),
('Marsabit', 'Marsabit'),
('Garissa', 'Garissa'),
('Wajir', 'Wajir'),
('Mandera', 'Mandera'),
('Tana River', 'Hola'),
('Lamu', 'Lamu'),
('Kilifi', 'Kilifi'),
('Taita Taveta', 'Voi'),
('Kwale', 'Kwale'),
('Turkana', 'Lodwar'),
('West Pokot', 'Kapenguria'),
('Samburu', 'Mararal'),
('Trans Nzoia', 'Kitale'),
('Uasin Gishu', 'Eldoret'),
('Elgeyo Marakwet', 'Iten'),
('Nandi', 'Kapsabet'),
('Baringo', 'Kabarnet'),
('Laikipia', 'Rumuruti'),
('Narok', 'Narok'),
('Kajiado', 'Kajiado'),
('Kericho', 'Kericho'),
('Bomet', 'Bomet'),
('Kakamega', 'Kakamega'),
('Vihiga', 'Vihiga'),
('Bungoma', 'Bungoma'),
('Busia', 'Busia'),
('Siaya', 'Siaya'),
('Homa Bay', 'Homa Bay'),
('Migori', 'Migori'),
('Kisii', 'Kisii'),
('Nyamira', 'Nyamira')
)

CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('IC', 'Icecreams'),
    ('CZ', 'Cheese'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    #selling_price = models.FilteredRelation()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    #discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
