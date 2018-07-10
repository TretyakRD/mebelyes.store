from django.http import JsonResponse, HttpResponse
from ..models import Product



def GetProduct(request):
    if request.method=='GET' and request.GET:

        idd = request.GET.get('id')

        product = Product.objects.filter(id=idd).values('id', 'name', 'prices', 'img_url', 'sizes', 'material')

        data = []

        for p in product:
            data.append({
                'id': p['id'],
                'name': p['name'],
                'prices': p['prices'],
                'img_url': p['img_url'],
                'sizes': p['sizes'],
                'material': p['material'],
            });

        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('Bad method!', status=500)