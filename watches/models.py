from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Watch(models.Model):

    # Watch brand - prefix brand options
    WATCH_BRAND = [
        ('ROLEX', 'ROLEX'),
        ('OMEGA', 'OMEGA'),
        ('HUBLOT', 'HUBLOT'),
    ]
    watch_brand = models.CharField(
        max_length=30,
        choices=WATCH_BRAND,
        default='ROLEX',
        blank=False
    )

    # Allow user to enter watch model
    watch_model = models.CharField(
        max_length=50,
        blank=False
    )

    # Description for the watch
    description = models.TextField(max_length=255)

    # Sale price of the watch
    price = models.DecimalField(
        blank=False,
        max_digits=9,
        decimal_places=2
    )

    # Watch available for sale
    STATUS = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default='Available'
    )

    # Picture for the watch
    cover = CloudinaryField('image')

    def __str__(self):
        return (self.watch_brand + " " + self.watch_model)
