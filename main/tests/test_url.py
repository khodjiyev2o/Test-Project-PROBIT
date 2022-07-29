from django.test import SimpleTestCase
from django.urls import reverse,resolve
from main.views import index,ProductDetailView

class TestUrls(SimpleTestCase):

    def test_index_urls(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func,index)
        
    def test_view_car_urls(self):
        url = reverse('car-view',args=['1'])
        self.assertEquals(resolve(url).func.view_class,ProductDetailView)
        
 