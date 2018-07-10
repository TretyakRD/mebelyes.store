
from django.shortcuts import render
from django.urls import reverse


def GetProduct(request, idd):
    url = reverse('api:GetProduct')
    context={
        'GetProductURL':url+'?id='+idd
    }
    return render(request, 'main/GetProduct.html', context)