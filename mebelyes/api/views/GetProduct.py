from django.http import JsonResponse, HttpResponse
from ..models import Product



def GetProduct(request):
    if request.method=='GET' and request.GET:

        idd = request.GET.get('id')

        product = Product.objects.filter(id=idd).values('id', 'name', 'prices', 'img_url', 'sizes', 'material','category')

        servs = Product.objects.filter(id=idd).values('services', 'services__description', 'services__price', 'services__slug')

        data = []

        data_servs=[]

        for s in servs:
            data_servs.append({
                'id':s['services'],
                'description':s['services__description'],
                'prices':s['services__price'],
                'slug':s['services__slug']
            })


        for p in product:
            data.append({
                'id': p['id'],
                'name': p['name'],
                'prices': p['prices'],
                'img_url': p['img_url'],
                'sizes': p['sizes'],
                'material': p['material'],
                'category': p['category'],
                'services': data_servs
            })
            break

        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('Bad method!', status=500)