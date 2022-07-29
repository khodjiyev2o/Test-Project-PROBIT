from cProfile import label
from .models import Car,Brand
import django_filters
from django_filters import ChoiceFilter,NumberFilter,ModelChoiceFilter
from django import forms
import datetime
## choices for transmission,year and car-brand-names
CHOICES = (
     (1, 'Automatic'),
    (0, 'Manual'),
    (None,'Both'),
)
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
CAR_CHOICES=[car.brand for car in Car.objects.all()]


## filter for Car model class
class CarFilter(django_filters.FilterSet):
    ##filtering through the range year(min and max)
    start_date = ChoiceFilter(field_name='year',lookup_expr='gte', choices=YEAR_CHOICES,label='',widget=forms.Select(attrs={'class': 'form-control'}))
    end_date = ChoiceFilter(field_name='year',lookup_expr='lte', choices=YEAR_CHOICES,label='',widget=forms.Select(attrs={'class': 'form-control'}))
    
    
    ##filtering through the transmission ,if automatic then it is true, else Manual 
    automatic_transmission = ChoiceFilter(field_name='automatic_transmission',choices=CHOICES,label='',widget=forms.Select(attrs={'class': 'form-control'}))
    
    ##filtering by price (prices lower or equal price than input value will be shown)
    price = NumberFilter(field_name='price',lookup_expr='lte',label='',widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter your budget...'}))
    
    ## filtering by how much car has been driven (cars with less then input value will be shown)
    mileage = NumberFilter(field_name='mileage',lookup_expr='lte',label='',widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter the most km...'}))
    
    ##filtering by brands(Brand names will be shown only the ones who are present in the database)
    brand =  ModelChoiceFilter(
        queryset=Brand.objects.all(),
       widget=forms.Select(attrs={'class': 'form-control','placeholder':'Enter  price...'})
    )
    class Meta:
        model = Car
        fields = ['name','brand','price','mileage','automatic_transmission' ]
        ## Noone will filter by image :)
        exclude = 'image'