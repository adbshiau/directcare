from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('PPE', 'PPE'),
    ('Tests', 'Tests'),
    ('Cleaning', 'Cleaning'),
    ('Supplies', 'Supplies'),
    ('Equipment', 'Equipment'),
    ('Miscallaneous', 'Miscallaneous'),
)

class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    item_size = models.CharField(max_length=100, null=True)
    purchased_from = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    expiration_date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = 'Available Items'

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Order Requests'

    def __str__(self):
        return f'{self.order_quantity} {self.item} ordered by {self.staff.username}'