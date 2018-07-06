

from django.urls import path
from .views.GetMainPage import GetMainPage

app_name="main"

urlpatterns = [

    path('', GetMainPage, name="GetMainPage"),

]
