from django.http import HttpResponse

from ..product import com_product


def Add(request):
    form = com_product(request)
    if 'cart' not in request.session:
        request.session['cart'] = []
        request.session['total_price'] = 0
    temp = request.session['cart']
    temp2 = request.session['total_price']
    temp.append(form)
    temp2 += int(form['price'])
    for i in form['services']:
        temp2 += int(i['price'])
    request.session['cart'] = temp
    request.session['total_price'] = temp2
    return HttpResponse('OK', status=200)