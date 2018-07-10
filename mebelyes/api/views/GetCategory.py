import json

from django.http import JsonResponse, HttpResponse
from ..models import Product



def GetCategory(request):
    if request.method=='GET' and request.GET:

        category = request.GET.get('category')

        products = Product.objects.filter(category=category).values('id', 'name', 'prices', 'img_url');



        data = []

        for p in products:
            data.append({
                'id': p['id'],
                'name': p['name'],
                'start_price': json.loads(p['prices'])[0][0],
                'img_url': p['img_url'],
            })

        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('Bad method!', status=500)