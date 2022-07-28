from .models import Car,Brand
import django_filters
from django_filters import CharFilter,DateFilter
from django import forms


class ProductFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='year',lookup_expr='gte')
    end_date = DateFilter(field_name='year',lookup_expr='lte')
 

    class Meta:
        model = Car
        fields = '__all__'
        exclude = 'image'