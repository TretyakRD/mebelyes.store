from django.urls import path
from .views.Add import Add
from .views.New import New

app_name = 'cart_order'

urlpatterns = [
    path('add', Add, name='Add'),
    path('new', New, name='New'),
]
