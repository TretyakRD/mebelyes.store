

from django.urls import path

from .views.GetProduct import GetProduct
from .views.GetMainPage import GetMainPage
from .views.GetCategory import GetCategory

app_name="main"

urlpatterns = [

    path('', GetMainPage, name="GetMainPage"),
    path('category/<category>', GetCategory, name="GetCategory"),
    path('product/<idd>', GetProduct, name="GetProduct"),
]
