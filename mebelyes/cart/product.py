
import json

from api.models.Product import Product
from api.models.Service import Service


def com_product(request):
    BD_product = Product.objects.get(id=request.POST.get('id'))
    prices = json.loads(BD_product.prices)
    mats = json.loads(BD_product.material.replace('\'', '\"'))
    sizes = json.loads(BD_product.sizes.replace('\'', '\"'))
    services_arr = '[' + request.POST.get('services') + ']'
    services_arr = json.loads(services_arr)

    services = Service.objects.filter(id__in=services_arr).values('description', 'price')

    services_arr = []

    for el in services:
        services_arr.append({
            'description' : el['description'],
            'price': json.loads(el['price'])[int(request.POST.get('material'))][int(request.POST.get('size'))]
        })

    return {
        'material': mats[int(request.POST.get('material'))],
        'size': sizes[int(request.POST.get('size'))],
        'color': request.POST.get('color'),
        'category': request.POST.get('category'),
        'id': request.POST.get('id'),
        'name': request.POST.get('name'),
        'price': prices[int(request.POST.get('material'))][int(request.POST.get('size'))],
        'services': services_arr
    }




