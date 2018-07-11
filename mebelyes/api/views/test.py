from django.http import HttpResponse

from ..models.Product import Product
from ..models.Service import Service

def test(request):
    items = Product.objects.filter(category='tahta')
    serv = Service.objects.all()
    iter = 0
    for el in items:
        iter += 1
        for it in serv:
            el.services.add(it)
        el.save()
    return HttpResponse(iter)

