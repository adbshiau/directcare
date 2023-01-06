from django.db import models

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

    def __str__(self):
        return f'{self.name} - {self.quantity}'