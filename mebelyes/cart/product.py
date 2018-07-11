
import json

from api.models.Product import Product


def com_product(request):
    BD_product = Product.objects.get(id=request.POST.get('id'))
    prices = json.loads(BD_product.prices)
    mats = json.loads(BD_product.material.replace('\'', '\"'))
    sizes = json.loads(BD_product.sizes.replace('\'', '\"'))
    return {
        'material': mats[int(request.POST.get('material'))],
        'size': sizes[int(request.POST.get('size'))],
        'color': request.POST.get('color'),
        'category': request.POST.get('category'),
        'id': request.POST.get('id'),
        'name': request.POST.get('name'),
        'price': prices[int(request.POST.get('material'))][int(request.POST.get('size'))]
    }




