from cProfile import label
from .models import Car,Brand
import django_filters
from django_filters import ChoiceFilter,NumberFilter,ModelChoiceFilter
from django import forms
import datetime
CHOICES = (
     (1, 'Automatic'),
    (0, 'Manual'),
    (None,'Both'),
)
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
CAR_CHOICES=[car.brand for car in Car.objects.all()]

class CarFilter(django_filters.FilterSet):
    start_date = ChoiceFilter(field_name='year',lookup_expr='gte', choices=YEAR_CHOICES,label='',widget=forms.Select(attrs={'class': 'form-control'}))
    end_date = ChoiceFilter(field_name='year',lookup_expr='lte', choices=YEAR_CHOICES,label='',widget=forms.Select(attrs={'class': 'form-control'}))
    automatic_transmission = ChoiceFilter(field_name='automatic_transmission',choices=CHOICES,label='',widget=forms.Select(attrs={'class': 'form-control'}))
    price = NumberFilter(field_name='price',label='',widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter  price...'}))
    mileage = NumberFilter(field_name='mileage',lookup_expr='gte',label='',widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter  km...'}))
    brand =  ModelChoiceFilter(
        queryset=Brand.objects.all(),
       widget=forms.Select(attrs={'class': 'form-control','placeholder':'Enter  price...'})
    )
    class Meta:
        model = Car
        fields = ['name','brand','price','mileage','automatic_transmission' ]
        exclude = 'image'