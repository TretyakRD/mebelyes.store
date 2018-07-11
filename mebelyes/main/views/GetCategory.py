
from django.shortcuts import render
from django.urls import reverse


def GetCategory(request, category):

    url = reverse('api:GetCategory')
    url_p = "/product/"
    context={
        'GetCategoryURL':url+'?category='+category,
        'GetProductURL':url_p
    }
    return render(request, 'main/GetCategory.html', context)