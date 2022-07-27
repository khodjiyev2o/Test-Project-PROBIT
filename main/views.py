from django.shortcuts import render
from .models import Car
from .filters  import  ProductFilter
# Create your views here.

def index(request):
    f = ProductFilter(request.GET, queryset=Car.objects.all())
    return render(request,'main/index.html',{'f':f})