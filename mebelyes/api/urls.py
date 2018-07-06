

from .views.GetProduct import GetProduct
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('', GetProduct, name='GetProduct'),
]
