from django.db import models

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=100)
    itemCost = models.CharField(max_length=100)
    itemId = models.IntegerField(default=0)

    def __str__(self):
        return self.itemName
    