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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cars'] = Car.objects.all()
        f = CarFilter(self.request.GET, queryset=Car.objects.all())
        context['forms'] = f
        return context