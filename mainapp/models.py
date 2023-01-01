from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=70)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name