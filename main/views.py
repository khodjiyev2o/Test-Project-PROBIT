from django.shortcuts import render
from .models import Car
from .filters  import  CarFilter
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    cars = Car.objects.all()
    f = CarFilter(request.GET, queryset=Car.objects.all())
    cars = f.qs
    return render(request,'main/index.html',{'forms':f,'cars':cars})



class ProductDetailView(DetailView):
    model = Car
    template_name = 'main/car_detail.html'
    context_object_name = "car"