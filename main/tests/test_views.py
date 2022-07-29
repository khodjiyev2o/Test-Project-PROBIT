from django.test import TestCase,Client
from django.urls import reverse
from main.models import Car,Brand


class TestViews(TestCase):
    def setUp(self):
        brand = Brand.objects.create(name='BMW')
        car = Car.objects.create(
            brand=brand,
            name="M-8",
            color='black',
            year=1999,
            mileage=22500,
            price=45000,
            automatic_transmission=True,
            )
        self.client = Client()
        self.index_url = reverse('index')
        self.car_detail_url = reverse('car-view',args=["1"])

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'main/index.html')

    def test_car_detail_view(self):
        response = self.client.get(self.car_detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'main/car_detail.html')


