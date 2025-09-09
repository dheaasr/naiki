from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    color = models.CharField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField()
    comment = models.TextField()
    rating = models.IntegerField()
    is_featured = models.BooleanField()

    def __str__(self):
        return self.name