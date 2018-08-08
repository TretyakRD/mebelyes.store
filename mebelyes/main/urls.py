

from django.urls import path

from .views.Offer import Offer
from .views.GetProduct import GetProduct
from .views.GetMainPage import GetMainPage
from .views.GetCategory import GetCategory
from .views.robots import robots

app_name="main"

urlpatterns = [

    path('', GetMainPage, name="GetMainPage"),
    path('category/<category>', GetCategory, name="GetCategory"),
    path('product/<idd>', GetProduct, name="GetProduct"),
    path('offer', Offer, name="Offer"),
    path('robots.txt', robots, name="robots")
]
