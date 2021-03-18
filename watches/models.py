from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


class Watch(models.Model):
    # User details
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

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
        max_length=100,
        blank=False
    )

    # Description for the watch
    description = models.TextField(max_length=500)

    # Sale price of the watch
    price = models.IntegerField(
        blank=False,
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
