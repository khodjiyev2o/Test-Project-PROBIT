from .models import Car,Brand
import django_filters
from django_filters import CharFilter
from django import forms


class ProductFilter(django_filters.FilterSet):
    
 

    class Meta:
        model = Car
        fields = ['year']