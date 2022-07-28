from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:pk>/view',views.ProductDetailView.as_view(),name='car-view')
]
