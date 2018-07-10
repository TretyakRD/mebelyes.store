import json

from django.http import JsonResponse, HttpResponse
from ..models import Product



def GetProduct(request):
    if request.method=='GET' and request.GET:

        id = request.GET.get('id')

        product = Product.objects.filter(id=id);

d        data = dict(product)
        a=1
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('Bad method!', status=500)