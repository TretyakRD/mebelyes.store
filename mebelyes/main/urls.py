

from django.urls import path
from .views.GetMainPage import GetMainPage
from .views.GetCategory import GetCategory

app_name="main"

urlpatterns = [

    path('', GetMainPage, name="GetMainPage"),
    path('category/<category>', GetCategory, name="GetCategory"),
]
