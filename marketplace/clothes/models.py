from django.db import models
from django.conf import settings


# Create your models here.
class Garment(models.Model):
    """Garment model"""

    class Size(models.TextChoices):
        """ Size Choices """
        SMALL = 'SM', 'Small'
        MEDIUM = 'MD', 'Medium'
        LARGE = 'LG', 'Large'

    class Type(models.TextChoices):
        """ Type Choices """
        SHIRT = 'SH', 'Shirt'
        PANTS = 'PA', 'Pants'
        JACKET = 'JA', 'Jacket'
        TSHIRT = 'TS', 'T-Shirt'
        SKIRT = 'SK', 'Skirt'
        DRESS = 'DR', 'Dress'
        OTHER = 'OT', 'Other'


    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(
        max_length=2,
        choices=Size.choices,
        default=Size.MEDIUM,
    )
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.SHIRT,
    )



