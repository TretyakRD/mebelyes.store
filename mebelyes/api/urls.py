

from .views.GetProduct import GetProduct
from .views.GetCategory import GetCategory
from .views.test import test
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('product', GetProduct, name='GetProduct'),
    path('category', GetCategory, name='GetCategory'),
    path('test', test, name='test'),
]
