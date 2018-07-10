
from django.shortcuts import render
from django.urls import reverse


def GetCategory(request, category):
    url = reverse('api:GetCategory')
    context={
        'GetCategoryURL':url+'?category='+category
    }
    return render(request, 'main/GetCategory.html', context)