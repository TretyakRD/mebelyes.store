from django.urls import path
from .views.GetCart import GetCart
from .views.Add import Add
from .views.RemoveFromCart import RemoveFromCart

app_name = "cart"

urlpatterns = [
    path('add', Add, name="Add"),
    path('', GetCart, name="GetCart"),
    path('remove', RemoveFromCart, name="RemoveFromCart"),
]
