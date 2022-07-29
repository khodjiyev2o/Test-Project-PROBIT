from django.test import TestCase,Client
from django.urls import reverse
from main.models import Brand,Car



class TestModels(TestCase):
    def setUp(self):
        brand = Brand.objects.create(name='BWM')
        car = Car.objects.create(
            brand=brand,
            name="M-8",
            color='black',
            year=1999,
            mileage=22500,
            price=45000,
            automatic_transmission=True,
            )
    def test_brand_create(self):
        self.assertEquals(Brand.objects.count(),1)
       

    def test_car(self):
        self.assertEquals(Car.objects.count(),1)
    