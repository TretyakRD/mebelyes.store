

from .views.GetProduct import GetProduct
from .views.GetCategory import GetCategory
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('product', GetProduct, name='GetProduct'),
    path('category', GetCategory, name='GetCategory'),
]
