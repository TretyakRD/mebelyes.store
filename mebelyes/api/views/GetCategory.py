from django.http import JsonResponse, HttpResponse
import json
from ..models import Product



def GetCategory(request):
    if request.method=='GET' and request.GET:

        category = request.GET.get('category')

        products = Product.objects.filter(category=category)

        data = []

        for p in products:
            data.append({
                'name': p.name,
                'slug': p.slug,
                'prices': p.prices,
                'description': p.description,
                'category': p.category,
                'material': p.material,
                'sizes': p.sizes,
                'img_url': p.img_url,
            })

        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('Bad method!', status=500)