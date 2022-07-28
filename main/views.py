from django.shortcuts import render
from .models import Car
from .filters  import  ProductFilter
# Create your views here.

def index(request):
    cars = Car.objects.all()
    f = ProductFilter(request.GET, queryset=Car.objects.all())
    cars = f.qs
    return render(request,'main/index.html',{'f':f,'cars':cars})