from django.urls import path

from .views.CalcDelv import CalcDelv
from .views.GetMap import GetMap

app_name = 'map'

urlpatterns = [
    path('calcdelv', CalcDelv, name='calcdelv'),
    path('getmap', GetMap, name='getmap'),
]
