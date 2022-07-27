from django.db import models

# Create your models here.

import datetime

YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
 

class Brand(models.Model):
    name = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return str(self.name)

class Car(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    mileage = models.IntegerField()
    rating = models.IntegerField()
    price = models.IntegerField()
    automatic_transmission = models.BooleanField(default=True)



    def __str__(self):
        return str(self.name)
